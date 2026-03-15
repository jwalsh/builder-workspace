"""SkillTreeExplorer — Interactive skill tree visualization and tracking.

A Flask web app for Replit deployment. Lets users visualize skill trees,
track progress, and discover learning paths.
"""

import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, g, jsonify, redirect, render_template_string, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-in-production")

DB_PATH = Path("data/skills.db")

# Skill tree data (embedded for Replit simplicity)
SKILL_TREES = {
    "backend": {
        "name": "Backend Engineering",
        "skills": [
            {"id": "http", "name": "HTTP & REST", "level": 1, "deps": [], "desc": "Understanding HTTP methods, status codes, REST principles"},
            {"id": "sql", "name": "SQL & Databases", "level": 1, "deps": [], "desc": "Relational databases, queries, joins, indexes"},
            {"id": "auth", "name": "Authentication", "level": 2, "deps": ["http"], "desc": "JWT, OAuth, session management, security"},
            {"id": "api-design", "name": "API Design", "level": 2, "deps": ["http"], "desc": "OpenAPI, versioning, pagination, error handling"},
            {"id": "orm", "name": "ORM & Data Layer", "level": 2, "deps": ["sql"], "desc": "SQLAlchemy, ActiveRecord, query optimization"},
            {"id": "caching", "name": "Caching", "level": 3, "deps": ["sql", "http"], "desc": "Redis, Memcached, cache invalidation strategies"},
            {"id": "queues", "name": "Message Queues", "level": 3, "deps": ["api-design"], "desc": "RabbitMQ, Kafka, async processing patterns"},
            {"id": "microservices", "name": "Microservices", "level": 4, "deps": ["api-design", "queues", "caching"], "desc": "Service decomposition, communication, resilience"},
        ]
    },
    "frontend": {
        "name": "Frontend Engineering",
        "skills": [
            {"id": "html-css", "name": "HTML & CSS", "level": 1, "deps": [], "desc": "Semantic HTML, CSS layout, responsive design"},
            {"id": "js-basics", "name": "JavaScript Basics", "level": 1, "deps": [], "desc": "Variables, functions, DOM manipulation, events"},
            {"id": "css-frameworks", "name": "CSS Frameworks", "level": 2, "deps": ["html-css"], "desc": "Tailwind, Bootstrap, design systems"},
            {"id": "react", "name": "React", "level": 2, "deps": ["js-basics"], "desc": "Components, hooks, state management"},
            {"id": "typescript", "name": "TypeScript", "level": 2, "deps": ["js-basics"], "desc": "Types, interfaces, generics"},
            {"id": "testing", "name": "Frontend Testing", "level": 3, "deps": ["react"], "desc": "Jest, Testing Library, E2E with Playwright"},
            {"id": "perf", "name": "Performance", "level": 3, "deps": ["react", "css-frameworks"], "desc": "Core Web Vitals, lazy loading, code splitting"},
            {"id": "a11y", "name": "Accessibility", "level": 3, "deps": ["html-css", "react"], "desc": "WCAG, screen readers, semantic markup"},
        ]
    },
    "devops": {
        "name": "DevOps & Infrastructure",
        "skills": [
            {"id": "linux", "name": "Linux & Shell", "level": 1, "deps": [], "desc": "Command line, scripting, file system, processes"},
            {"id": "git", "name": "Git & Version Control", "level": 1, "deps": [], "desc": "Branching, merging, rebasing, workflows"},
            {"id": "docker", "name": "Docker", "level": 2, "deps": ["linux"], "desc": "Containers, images, Dockerfile, compose"},
            {"id": "ci-cd", "name": "CI/CD", "level": 2, "deps": ["git"], "desc": "GitHub Actions, pipelines, automated testing"},
            {"id": "k8s", "name": "Kubernetes", "level": 3, "deps": ["docker"], "desc": "Pods, services, deployments, helm"},
            {"id": "monitoring", "name": "Monitoring", "level": 3, "deps": ["docker", "ci-cd"], "desc": "Prometheus, Grafana, alerting, SLOs"},
            {"id": "iac", "name": "Infrastructure as Code", "level": 3, "deps": ["docker"], "desc": "Terraform, Pulumi, CloudFormation"},
            {"id": "sre", "name": "SRE Practices", "level": 4, "deps": ["k8s", "monitoring", "iac"], "desc": "Incident response, postmortems, error budgets"},
        ]
    },
}


def get_db():
    if "db" not in g:
        DB_PATH.parent.mkdir(exist_ok=True)
        g.db = sqlite3.connect(str(DB_PATH))
        g.db.row_factory = sqlite3.Row
        g.db.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                user_id TEXT DEFAULT 'default',
                tree_id TEXT NOT NULL,
                skill_id TEXT NOT NULL,
                completed_at TEXT,
                PRIMARY KEY (user_id, tree_id, skill_id)
            )
        """)
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db:
        db.close()


TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skill Tree Explorer</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: system-ui, sans-serif; background: #0d1117; color: #c9d1d9; }
.container { max-width: 900px; margin: 0 auto; padding: 20px; }
h1 { color: #58a6ff; margin-bottom: 8px; }
.subtitle { color: #8b949e; margin-bottom: 24px; }
.trees { display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
.tree-btn { padding: 8px 16px; border: 1px solid #30363d; background: #21262d;
  color: #c9d1d9; border-radius: 6px; cursor: pointer; text-decoration: none; }
.tree-btn:hover { background: #30363d; }
.tree-btn.active { background: #1f6feb; border-color: #1f6feb; color: white; }
.level { margin-bottom: 20px; }
.level-label { color: #8b949e; font-size: 12px; text-transform: uppercase;
  letter-spacing: 1px; margin-bottom: 8px; }
.skills { display: flex; gap: 10px; flex-wrap: wrap; }
.skill { padding: 12px 16px; border: 1px solid #30363d; border-radius: 8px;
  background: #161b22; cursor: pointer; min-width: 160px; transition: all 0.2s; }
.skill:hover { border-color: #58a6ff; }
.skill.completed { border-color: #3fb950; background: #0d1117; }
.skill.locked { opacity: 0.4; cursor: not-allowed; }
.skill-name { font-weight: 600; margin-bottom: 4px; }
.skill-desc { font-size: 12px; color: #8b949e; }
.skill-deps { font-size: 11px; color: #f0883e; margin-top: 4px; }
.progress { margin-bottom: 24px; padding: 12px; background: #161b22;
  border-radius: 6px; border: 1px solid #30363d; }
.bar { height: 8px; background: #21262d; border-radius: 4px; overflow: hidden; }
.bar-fill { height: 100%; background: #3fb950; border-radius: 4px; transition: width 0.3s; }
.stats { display: flex; justify-content: space-between; margin-top: 8px; font-size: 13px; color: #8b949e; }
</style>
</head>
<body>
<div class="container">
<h1>Skill Tree Explorer</h1>
<p class="subtitle">Track your learning progress across engineering disciplines</p>

<div class="trees">
{% for tid, tree in trees.items() %}
<a href="?tree={{ tid }}" class="tree-btn {{ 'active' if tid == current_tree }}">
  {{ tree.name }}
</a>
{% endfor %}
</div>

{% if tree %}
<div class="progress">
  <div class="bar"><div class="bar-fill" style="width: {{ progress_pct }}%"></div></div>
  <div class="stats">
    <span>{{ completed_count }}/{{ total_count }} skills completed</span>
    <span>{{ progress_pct }}%</span>
  </div>
</div>

{% for level_num in levels %}
<div class="level">
  <div class="level-label">Level {{ level_num }}</div>
  <div class="skills">
    {% for skill in tree.skills if skill.level == level_num %}
    <form method="POST" style="display:inline">
      <input type="hidden" name="skill_id" value="{{ skill.id }}">
      <input type="hidden" name="tree_id" value="{{ current_tree }}">
      <button type="submit" class="skill {{ 'completed' if skill.id in completed }} {{ 'locked' if skill.id in locked }}"
        {{ 'disabled' if skill.id in locked }}>
        <div class="skill-name">{{ '✓ ' if skill.id in completed }}{{ skill.name }}</div>
        <div class="skill-desc">{{ skill.desc }}</div>
        {% if skill.deps %}
        <div class="skill-deps">Requires: {{ skill.deps | join(', ') }}</div>
        {% endif %}
      </button>
    </form>
    {% endfor %}
  </div>
</div>
{% endfor %}
{% endif %}
</div>
</body>
</html>"""


@app.route("/", methods=["GET", "POST"])
def index():
    db = get_db()

    if request.method == "POST":
        tree_id = request.form["tree_id"]
        skill_id = request.form["skill_id"]
        existing = db.execute(
            "SELECT 1 FROM progress WHERE tree_id=? AND skill_id=?",
            (tree_id, skill_id),
        ).fetchone()
        if existing:
            db.execute("DELETE FROM progress WHERE tree_id=? AND skill_id=?", (tree_id, skill_id))
        else:
            db.execute(
                "INSERT INTO progress (tree_id, skill_id, completed_at) VALUES (?, ?, ?)",
                (tree_id, skill_id, datetime.utcnow().isoformat()),
            )
        db.commit()
        return redirect(url_for("index", tree=tree_id))

    current_tree = request.args.get("tree", "backend")
    tree = SKILL_TREES.get(current_tree)

    completed = set()
    if tree:
        rows = db.execute("SELECT skill_id FROM progress WHERE tree_id=?", (current_tree,)).fetchall()
        completed = {r["skill_id"] for r in rows}

    locked = set()
    if tree:
        for skill in tree["skills"]:
            if skill["deps"] and not all(d in completed for d in skill["deps"]):
                locked.add(skill["id"])

    levels = sorted(set(s["level"] for s in tree["skills"])) if tree else []
    total = len(tree["skills"]) if tree else 0
    done = len(completed)
    pct = int(done / total * 100) if total else 0

    return render_template_string(
        TEMPLATE,
        trees=SKILL_TREES,
        tree=tree,
        current_tree=current_tree,
        completed=completed,
        locked=locked,
        levels=levels,
        completed_count=done,
        total_count=total,
        progress_pct=pct,
    )


@app.route("/api/trees")
def api_trees():
    return jsonify({tid: t["name"] for tid, t in SKILL_TREES.items()})


@app.route("/api/tree/<tree_id>")
def api_tree(tree_id):
    tree = SKILL_TREES.get(tree_id)
    if not tree:
        return jsonify({"error": "not found"}), 404
    db = get_db()
    rows = db.execute("SELECT skill_id FROM progress WHERE tree_id=?", (tree_id,)).fetchall()
    completed = [r["skill_id"] for r in rows]
    return jsonify({**tree, "completed": completed})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)

#!/usr/bin/env python3
"""Generate spec.org files for all projects in the workspace.

Reads each project's config/project_info.json and config/tasks.json
to produce a structured spec.org suitable for the bootstrap protocol.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime


PROJECTS_DIR = Path(__file__).parent.parent / "projects"


def load_json(path: Path) -> dict | list | None:
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def get_category(project_dir: Path) -> str:
    """Get category from top-level project_info.json."""
    info = load_json(project_dir / "project_info.json")
    if info and isinstance(info, dict):
        return info.get("category", "UNKNOWN")
    return "UNKNOWN"


def topological_sort_tasks(tasks: list[dict]) -> list[dict]:
    """Sort tasks respecting dependencies, falling back to priority."""
    title_to_task = {t["title"]: t for t in tasks}
    # Also match partial titles for deps
    visited = set()
    result = []

    def visit(task):
        if task["title"] in visited:
            return
        visited.add(task["title"])
        for dep_title in task.get("dependencies", []):
            # Find matching task (deps may be partial matches)
            for t in tasks:
                if dep_title in t["title"] or t["title"] in dep_title:
                    visit(t)
                    break
        result.append(task)

    # Sort by priority descending (5=highest) then by id
    for task in sorted(tasks, key=lambda t: (-t.get("priority", 0), t.get("id", 0))):
        visit(task)

    return result


def extract_conjectures(project_name: str, description: str, tasks: list[dict]) -> list[dict]:
    """Derive conjectures from project description and tasks."""
    conjectures = []
    conjecture_id = 1

    # Core feasibility conjecture
    conjectures.append({
        "id": f"C-{conjecture_id:03d}",
        "claim": f"{project_name} can deliver its core value proposition as described",
        "falsification": "Integration test of end-to-end workflow fails to produce expected output"
    })
    conjecture_id += 1

    # Check for AI/ML tasks
    ai_tasks = [t for t in tasks if any(kw in t.get("description", "").lower()
                for kw in ["ai", "ml", "machine learning", "neural", "model", "training"])]
    if ai_tasks:
        conjectures.append({
            "id": f"C-{conjecture_id:03d}",
            "claim": "AI/ML components achieve sufficient accuracy for production use",
            "falsification": "Model accuracy on held-out test set falls below domain-specific threshold"
        })
        conjecture_id += 1

    # Check for real-time requirements
    rt_tasks = [t for t in tasks if any(kw in t.get("description", "").lower()
                for kw in ["real-time", "realtime", "real time", "streaming", "latency"])]
    if rt_tasks:
        conjectures.append({
            "id": f"C-{conjecture_id:03d}",
            "claim": "System meets real-time latency requirements under load",
            "falsification": "P95 latency exceeds target under simulated production load"
        })
        conjecture_id += 1

    # Check for scalability concerns
    scale_tasks = [t for t in tasks if any(kw in t.get("description", "").lower()
                   for kw in ["scalab", "distributed", "concurrent", "throughput"])]
    if scale_tasks:
        conjectures.append({
            "id": f"C-{conjecture_id:03d}",
            "claim": "Architecture scales horizontally to meet projected demand",
            "falsification": "Load test shows non-linear degradation before target throughput"
        })
        conjecture_id += 1

    # Check for security tasks
    sec_tasks = [t for t in tasks if any(kw in t.get("description", "").lower()
                 for kw in ["security", "encryption", "auth", "vulnerab"])]
    if sec_tasks:
        conjectures.append({
            "id": f"C-{conjecture_id:03d}",
            "claim": "Security implementation meets compliance requirements",
            "falsification": "Penetration test or security audit reveals critical vulnerability"
        })
        conjecture_id += 1

    return conjectures


def derive_stack(tasks: list[dict], description: str) -> list[str]:
    """Derive likely technology stack from task descriptions."""
    all_text = description + " " + " ".join(t.get("description", "") for t in tasks)
    all_text_lower = all_text.lower()

    stack = []
    tech_keywords = {
        "Python": ["python", "flask", "django", "fastapi", "pytest"],
        "TypeScript/JavaScript": ["typescript", "javascript", "react", "angular", "vue", "node", "next.js"],
        "Rust": ["rust", "cargo"],
        "Go": ["golang", " go "],
        "Java": ["java", "spring", "maven"],
        "PostgreSQL": ["postgresql", "postgres"],
        "MongoDB": ["mongodb", "mongo"],
        "Redis": ["redis"],
        "Docker": ["docker", "container"],
        "Kubernetes": ["kubernetes", "k8s"],
        "AWS": ["aws", "amazon", "lambda", "s3"],
        "TensorFlow": ["tensorflow"],
        "PyTorch": ["pytorch"],
        "GraphQL": ["graphql"],
        "REST API": ["restful", "rest api"],
    }

    for tech, keywords in tech_keywords.items():
        if any(kw in all_text_lower for kw in keywords):
            stack.append(tech)

    if not stack:
        stack.append("Python (default)")

    return stack


def generate_spec_org(project_dir: Path) -> str | None:
    """Generate spec.org content for a project."""
    config_dir = project_dir / "config"

    # Load project info
    info = load_json(config_dir / "project_info.json")
    if not info or not isinstance(info, dict):
        return None

    name = info.get("name", project_dir.name)
    description = info.get("description", "No description available.")
    created_at = info.get("created_at", "")

    # Load tasks
    tasks = load_json(config_dir / "tasks.json")
    if not tasks or not isinstance(tasks, list):
        tasks = []

    # Get category
    category = get_category(project_dir)

    # Sort tasks
    sorted_tasks = topological_sort_tasks(tasks)

    # Extract RFCs
    rfcs = [t for t in tasks if t.get("task_type") == "rfc"]

    # Extract implementation tasks
    impl_tasks = [t for t in tasks if t.get("task_type") != "rfc"]

    # Derive conjectures
    conjectures = extract_conjectures(name, description, tasks)

    # Derive stack
    stack = derive_stack(tasks, description)

    # Check for RFCs directory
    rfc_files = []
    rfc_dir = project_dir / "rfcs"
    if rfc_dir.is_dir():
        rfc_files = sorted(rfc_dir.iterdir())

    # Build the spec.org
    lines = []
    lines.append(f"#+TITLE: {name}")
    lines.append(f"#+SUBTITLE: {description}")
    lines.append(f"#+CATEGORY: {category}")
    lines.append(f"#+DATE: {created_at[:10] if created_at else 'unknown'}")
    lines.append(f"#+STARTUP: overview")
    lines.append("")

    # Overview
    lines.append("* Overview")
    lines.append("")
    lines.append(f"{description}")
    lines.append("")

    # Foundational Axiom
    lines.append("* Foundational Axiom")
    lines.append("")

    # Derive axiom from description
    # The axiom should capture why this project exists
    axiom = _derive_axiom(name, description, category)
    lines.append(axiom)
    lines.append("")

    # Anti-Goals
    lines.append("* Anti-Goals")
    lines.append("")
    anti_goals = _derive_anti_goals(name, description, category)
    for ag in anti_goals:
        lines.append(f"- {ag}")
    lines.append("")

    # Architecture
    if rfcs:
        lines.append("* Architectural Decisions")
        lines.append("")
        for rfc in rfcs:
            lines.append(f"** {rfc['title']}")
            lines.append(f"   :STATUS: {rfc.get('rfc_state', 'UNKNOWN')}")
            # Truncate very long descriptions
            desc = rfc.get("description", "")
            if len(desc) > 500:
                desc = desc[:500] + "..."
            lines.append(f"   {desc}")
            lines.append("")

    # Build Order
    lines.append("* Build Order")
    lines.append("")
    for i, task in enumerate(sorted_tasks, 1):
        status_marker = {
            "TODO": "TODO",
            "IN_PROGRESS": "IN_PROGRESS",
            "IMPLEMENTATION": "IN_PROGRESS",
            "READY_FOR_IMPLEMENTATION": "TODO",
            "READY_FOR_APPROVAL": "TODO",
            "REVIEW_COMPLETE": "DONE",
            "DONE": "DONE",
        }.get(task.get("status", "TODO"), "TODO")

        deps_str = ""
        if task.get("dependencies"):
            deps_str = f" (depends on: {', '.join(task['dependencies'])})"

        lines.append(f"** {status_marker} Step {i}: {task['title']}")
        lines.append(f"   :PRIORITY: {task.get('priority', 3)}")
        lines.append(f"   :ASSIGNED: {task.get('assigned_to', 'unassigned')}")
        if deps_str:
            lines.append(f"   :DEPENDS:{deps_str}")

        desc = task.get("description", "")
        if len(desc) > 300:
            desc = desc[:300] + "..."
        lines.append(f"   {desc}")
        lines.append("")
        lines.append(f"   *Acceptance test*: {task['title']} component is implemented, tested, and integrated.")
        lines.append("")

    # Failure handler
    lines.append("** Failure Handler")
    lines.append("   If an acceptance test fails, stop. Document what failed,")
    lines.append("   what you tried, and what the blocker is. Do not proceed")
    lines.append("   to the next step. Surface the failure as a CPRR refutation")
    lines.append("   candidate.")
    lines.append("")

    # Conjectures
    lines.append("* Open Conjectures")
    lines.append("")
    for c in conjectures:
        lines.append(f"** {c['id']}: {c['claim']}")
        lines.append(f"   :FALSIFICATION: {c['falsification']}")
        lines.append("")

    # Stack
    lines.append("* Stack Preferences")
    lines.append("")
    for s in stack:
        lines.append(f"- {s}")
    lines.append("")

    # Success Criteria
    lines.append("* Success Criteria")
    lines.append("")
    lines.append(f"1. All build steps completed with passing acceptance tests")
    lines.append(f"2. End-to-end workflow demonstrates core value: {description[:100]}")
    lines.append(f"3. All open conjectures either confirmed with evidence or refuted with data")
    lines.append(f"4. System deployed and accessible to primary users")
    lines.append("")

    # Primary User and Output
    lines.append("* Primary User")
    lines.append("")
    primary_user = _derive_primary_user(description, category)
    lines.append(f"{primary_user}")
    lines.append("")

    lines.append("* Primary Output Artifact")
    lines.append("")
    primary_output = _derive_primary_output(description, category)
    lines.append(f"{primary_output}")
    lines.append("")

    # Research Context (RFC files if any)
    if rfc_files:
        lines.append("* Research Context")
        lines.append("")
        for rf in rfc_files:
            lines.append(f"- [[file:rfcs/{rf.name}][{rf.name}]]")
        lines.append("")

    return "\n".join(lines)


def _derive_axiom(name: str, description: str, category: str) -> str:
    """Derive a foundational axiom from the project description."""
    # Map categories to axiom patterns
    category_axioms = {
        "AI_ML": f"Existing tools treat {_extract_domain(description)} as a generic automation problem; {name} succeeds by encoding domain-specific structure that general-purpose AI cannot discover from data alone.",
        "SOFTWARE_ENGINEERING": f"The bottleneck in {_extract_domain(description)} is not compute or data but the feedback loop between intent and artifact; {name} compresses that loop.",
        "SECURITY": f"Security in {_extract_domain(description)} fails when it is bolted on after the fact; {name} makes security a structural property of the system rather than an additional layer.",
        "HEALTHCARE": f"Healthcare tools fail when they optimize for data collection over clinical workflow; {name} embeds clinical reasoning into the system's structure.",
        "ENVIRONMENTAL": f"Environmental tools fail when they model systems in isolation; {name} captures the cross-domain interactions that determine real-world outcomes.",
        "ENERGY": f"Energy systems fail when they optimize for peak efficiency at the cost of resilience; {name} maintains correctness across the full operating envelope.",
        "BCI": f"Brain-computer interfaces fail when they treat neural signals as simple input streams; {name} models the bidirectional adaptation between brain and system.",
        "EDUCATION": f"Educational tools fail when they optimize for content delivery over understanding; {name} closes the gap between instruction and verified comprehension.",
        "BIOTECH": f"Biotech tools fail when they treat biological systems as deterministic; {name} embraces stochasticity as a design constraint.",
        "QUANTUM": f"Quantum computing tools fail when they abstract away hardware constraints; {name} co-designs algorithms with the physical substrate.",
        "SIMULATION": f"Simulations fail when they sacrifice fidelity for speed without quantifying the trade-off; {name} makes approximation error explicit and bounded.",
        "AUTONOMOUS_SYSTEMS": f"Autonomous systems fail when they optimize for nominal conditions; {name} guarantees safe behavior across the full distribution of operating conditions.",
        "BLOCKCHAIN": f"Distributed systems fail when they conflate consensus with correctness; {name} separates mechanism from policy.",
        "INFRASTRUCTURE": f"Infrastructure tools fail when they treat configuration as static; {name} models infrastructure as a continuously evolving system.",
    }

    axiom = category_axioms.get(category,
        f"Existing approaches to {_extract_domain(description)} fail because they optimize for the common case while ignoring structural constraints; {name} makes those constraints first-class.")

    return axiom


def _extract_domain(description: str) -> str:
    """Extract a short domain phrase from description."""
    # Take first meaningful clause
    desc = description.lower()
    for prefix in ["an ", "a ", "the "]:
        if desc.startswith(prefix):
            desc = desc[len(prefix):]
    # Find the first clause boundary
    for sep in [" that ", " which ", " for ", " to "]:
        idx = desc.find(sep)
        if idx > 0 and idx < 80:
            return desc[:idx]
    return desc[:60].rstrip()


def _derive_anti_goals(name: str, description: str, category: str) -> list[str]:
    """Derive anti-goals from project context."""
    anti_goals = [
        f"*General-purpose platform*: {name} solves a specific problem, not a platform for all problems in this domain. Building a platform leads to feature sprawl and loss of core value.",
        f"*Manual-first workflow*: Do not build processes that require constant human intervention for routine operations. If a human must babysit it, the automation has failed.",
        f"*Demo-ware*: Do not optimize for impressive demos at the cost of production reliability. A system that works in a demo but fails under real conditions is worse than no system.",
    ]
    return anti_goals


def _derive_primary_user(description: str, category: str) -> str:
    """Derive primary user from description and category."""
    user_map = {
        "AI_ML": "ML engineers and data scientists who need production-grade AI capabilities",
        "SOFTWARE_ENGINEERING": "Software developers working in professional development environments",
        "SECURITY": "Security engineers and SOC analysts responsible for system protection",
        "HEALTHCARE": "Healthcare professionals (clinicians, administrators) in clinical settings",
        "ENVIRONMENTAL": "Environmental scientists and sustainability officers",
        "ENERGY": "Energy system operators and grid engineers",
        "BCI": "Neuroscientists and clinical researchers working with neural interfaces",
        "EDUCATION": "Educators and learners in structured learning environments",
        "BIOTECH": "Biotechnology researchers and lab scientists",
        "QUANTUM": "Quantum computing researchers and algorithm developers",
        "SIMULATION": "Engineers and researchers who need high-fidelity simulations",
        "AUTONOMOUS_SYSTEMS": "Robotics engineers and autonomous systems operators",
        "BLOCKCHAIN": "Distributed systems developers and protocol designers",
        "INFRASTRUCTURE": "DevOps engineers and infrastructure operators",
        "SOCIAL_MEDIA": "Content creators and community managers",
        "FINANCE": "Financial analysts and portfolio managers",
        "LEGAL": "Legal professionals and compliance officers",
        "ENTERTAINMENT": "Content creators and media producers",
        "MARKETING": "Marketing professionals and campaign managers",
        "PETS": "Pet owners and veterinary professionals",
        "HCI": "UX researchers and interaction designers",
        "DOCUMENTATION": "Technical writers and documentation teams",
        "PHILOSOPHY": "Researchers and educators in philosophy and ethics",
        "XR": "XR developers and spatial computing designers",
        "URBAN": "Urban planners and city administrators",
        "REAL_ESTATE": "Real estate professionals and property developers",
        "SPACE": "Aerospace engineers and space mission planners",
        "LOGISTICS": "Supply chain managers and logistics operators",
        "IOT": "IoT engineers and embedded systems developers",
        "TRAVEL": "Travel industry professionals and travelers",
        "HR": "HR professionals and talent acquisition teams",
        "RETAIL": "Retail managers and e-commerce operators",
        "GAMING": "Game developers and interactive media designers",
        "MANUFACTURING": "Manufacturing engineers and production managers",
        "AGRICULTURAL": "Agricultural scientists and farm operators",
    }
    return user_map.get(category, "Domain professionals who need specialized tooling")


def _derive_primary_output(description: str, category: str) -> str:
    """Derive primary output artifact."""
    desc_lower = description.lower()
    if "api" in desc_lower or "service" in desc_lower:
        return "A deployed service with documented API endpoints"
    elif "tool" in desc_lower:
        return "A production-ready tool with CLI and/or web interface"
    elif "platform" in desc_lower:
        return "A deployed platform with user-facing interface"
    elif "system" in desc_lower:
        return "An integrated system with monitoring and operational runbook"
    elif "engine" in desc_lower:
        return "A reusable engine with well-defined input/output contracts"
    elif "model" in desc_lower or "ai" in desc_lower:
        return "A trained model with evaluation metrics and serving infrastructure"
    elif "monitor" in desc_lower or "analyzer" in desc_lower:
        return "A monitoring/analysis dashboard with alerting capabilities"
    else:
        return "A working implementation with tests, documentation, and deployment guide"


def main():
    if not PROJECTS_DIR.is_dir():
        print(f"Error: {PROJECTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    projects = sorted(d for d in PROJECTS_DIR.iterdir() if d.is_dir())
    generated = 0
    skipped = 0
    errors = 0

    for project_dir in projects:
        config_dir = project_dir / "config"
        if not config_dir.is_dir():
            skipped += 1
            continue

        spec_path = project_dir / "spec.org"
        if spec_path.exists():
            skipped += 1
            continue

        try:
            content = generate_spec_org(project_dir)
            if content:
                with open(spec_path, "w") as f:
                    f.write(content)
                generated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"Error generating spec for {project_dir.name}: {e}", file=sys.stderr)
            errors += 1

    print(f"Generated: {generated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()

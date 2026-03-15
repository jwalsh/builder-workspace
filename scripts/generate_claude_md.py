#!/usr/bin/env python3
"""Generate CLAUDE.md files for all projects that have spec.org but no CLAUDE.md.

Parses each project's spec.org to produce a concise CLAUDE.md following
the bootstrap protocol structure.
"""

import os
import re
import sys
from pathlib import Path


PROJECTS_DIR = Path(__file__).parent.parent / "projects"


def parse_spec_org(spec_path: Path) -> dict:
    """Parse a spec.org file into structured data."""
    content = spec_path.read_text(errors="replace")

    data = {}

    # Title and subtitle
    m = re.search(r'#\+TITLE:\s*(.+)', content)
    data['name'] = m.group(1).strip() if m else spec_path.parent.name

    m = re.search(r'#\+SUBTITLE:\s*(.+)', content)
    data['subtitle'] = m.group(1).strip() if m else ''

    m = re.search(r'#\+CATEGORY:\s*(.+)', content)
    data['category'] = m.group(1).strip() if m else 'UNKNOWN'

    # Foundational Axiom
    m = re.search(r'\* Foundational Axiom\s*\n\s*\n(.+?)(?:\n\n|\n\*)', content, re.DOTALL)
    data['axiom'] = m.group(1).strip() if m else ''

    # Anti-Goals
    anti_goals = re.findall(r'- \*\*?(.+?)\*\*?:\s*(.+)', content)
    data['anti_goals'] = [(name.strip('*'), desc.strip()) for name, desc in anti_goals[:3]]

    # Build Order steps
    steps = []
    step_pattern = re.compile(
        r'\*\* (?:TODO|IN_PROGRESS|DONE) Step (\d+): (.+?)\n'
        r'(?:\s+:PRIORITY: (\d+)\n)?'
        r'(?:\s+:ASSIGNED: (.+?)\n)?'
        r'(?:\s+:DEPENDS:(.+?)\n)?',
        re.DOTALL
    )
    for m in step_pattern.finditer(content):
        step = {
            'num': int(m.group(1)),
            'title': m.group(2).strip(),
            'priority': m.group(3) or '3',
            'assigned': m.group(4) or 'unassigned',
            'depends': m.group(5).strip() if m.group(5) else '',
        }
        steps.append(step)
    data['steps'] = steps

    # Conjectures
    conjectures = []
    conj_pattern = re.compile(
        r'\*\* (C-\d+): (.+?)\n\s+:FALSIFICATION: (.+?)(?:\n|$)'
    )
    for m in conj_pattern.finditer(content):
        conjectures.append({
            'id': m.group(1),
            'claim': m.group(2).strip(),
            'falsification': m.group(3).strip(),
        })
    data['conjectures'] = conjectures

    # Stack
    stack_section = re.search(r'\* Stack Preferences\s*\n((?:\s*- .+\n)*)', content)
    if stack_section:
        data['stack'] = [line.strip('- \n') for line in stack_section.group(1).strip().split('\n') if line.strip()]
    else:
        data['stack'] = ['Python (default)']

    # Primary User
    m = re.search(r'\* Primary User\s*\n\s*\n(.+?)(?:\n\n|\n\*|$)', content, re.DOTALL)
    data['primary_user'] = m.group(1).strip() if m else 'Domain professionals'

    # Primary Output
    m = re.search(r'\* Primary Output Artifact\s*\n\s*\n(.+?)(?:\n\n|\n\*|$)', content, re.DOTALL)
    data['primary_output'] = m.group(1).strip() if m else 'A working implementation'

    # What to build - derive from subtitle
    data['what'] = _derive_what(data['name'], data['subtitle'], steps)

    return data


def _derive_what(name: str, subtitle: str, steps: list) -> list[str]:
    """Derive 2-3 bullet points for What You Are Building."""
    bullets = []

    # Find backend/API steps
    backend_steps = [s for s in steps if any(kw in s['title'].lower() for kw in ['backend', 'api', 'engine', 'service', 'processing', 'software'])]
    frontend_steps = [s for s in steps if any(kw in s['title'].lower() for kw in ['frontend', 'interface', 'ui', 'ux', 'visualization'])]
    data_steps = [s for s in steps if any(kw in s['title'].lower() for kw in ['database', 'data', 'storage', 'schema'])]

    if backend_steps:
        bullets.append(f"Backend services: {backend_steps[0]['title'].lower()}")
    elif subtitle:
        bullets.append(f"Core system: {subtitle[:100]}")

    if frontend_steps:
        bullets.append(f"User interface: {frontend_steps[0]['title'].lower()}")

    if data_steps:
        bullets.append(f"Data layer: {data_steps[0]['title'].lower()}")

    if not bullets:
        bullets = [
            f"Core implementation of {name}",
            f"Testing and quality assurance",
            f"Documentation and deployment",
        ]

    return bullets[:3]


def generate_claude_md(data: dict) -> str:
    """Generate CLAUDE.md content from parsed spec data."""
    lines = []

    # Title and role
    lines.append(f"# {data['name']}")
    lines.append("")
    lines.append(f"You are a coding agent working on {data['name']} -- {data['subtitle']}")
    lines.append("")

    # Axiom (MUST be before line 10)
    lines.append("## Foundational Axiom")
    lines.append("")
    lines.append(data['axiom'] or f"Existing approaches fail by ignoring structural constraints; {data['name']} makes those constraints first-class.")
    lines.append("")

    # Confirmation Gate
    lines.append("## Confirmation Gate")
    lines.append("")
    lines.append("Before writing any code, confirm:")
    lines.append("1. You have read `spec.org` in this directory.")
    lines.append("2. You understand the build order and current step.")
    lines.append("3. You will not skip a failing acceptance test.")
    lines.append("")

    # What You Are Building
    lines.append("## What You Are Building")
    lines.append("")
    for bullet in data['what']:
        lines.append(f"- {bullet}")
    lines.append("")

    # Anti-Goals
    lines.append("## Anti-Goals")
    lines.append("")
    if data['anti_goals']:
        for name, desc in data['anti_goals']:
            lines.append(f"- **{name}**: {desc}")
    else:
        lines.append("- **General-purpose platform**: Solve the specific problem, not all problems in the domain.")
        lines.append("- **Manual-first workflow**: If a human must babysit it, the automation has failed.")
        lines.append("- **Demo-ware**: Optimize for production reliability, not impressive demos.")
    lines.append("")

    # Build Order
    lines.append("## Build Order")
    lines.append("")
    for step in data['steps']:
        dep_str = f" -- {step['depends']}" if step['depends'] else ""
        lines.append(f"{step['num']}. {step['title']} (P{step['priority']}){dep_str}")
    lines.append("")
    lines.append("### Failure Handler")
    lines.append("")
    lines.append("If an acceptance test fails, STOP. Document what failed, what you tried, and the blocker. Do not proceed to the next step. Surface the failure as a CPRR refutation candidate.")
    lines.append("")

    # Conjectures
    if data['conjectures']:
        lines.append("## Open Conjectures")
        lines.append("")
        for c in data['conjectures']:
            lines.append(f"- **{c['id']}**: {c['claim']}")
            lines.append(f"  - Falsification: {c['falsification']}")
        lines.append("")

    # Stack
    lines.append("## Stack")
    lines.append("")
    for s in data['stack']:
        lines.append(f"- {s}")
    lines.append("")

    # Success Criteria
    lines.append("## Success Criteria")
    lines.append("")
    lines.append("1. All build steps completed with passing acceptance tests.")
    desc = data['subtitle'][:100] if data['subtitle'] else data['name']
    lines.append(f"2. End-to-end workflow demonstrates core value: {desc}.")
    lines.append("3. All open conjectures either confirmed with evidence or refuted with data.")
    lines.append(f"4. System deployed and accessible to {data['primary_user'].lower()}.")
    lines.append("")

    return "\n".join(lines)


def main():
    if not PROJECTS_DIR.is_dir():
        print(f"Error: {PROJECTS_DIR} not found", file=sys.stderr)
        sys.exit(1)

    generated = 0
    skipped = 0
    errors = 0

    for project_dir in sorted(PROJECTS_DIR.iterdir()):
        if not project_dir.is_dir():
            continue

        spec_path = project_dir / "spec.org"
        claude_path = project_dir / "CLAUDE.md"

        if not spec_path.exists():
            skipped += 1
            continue

        if claude_path.exists():
            skipped += 1
            continue

        try:
            data = parse_spec_org(spec_path)
            content = generate_claude_md(data)
            claude_path.write_text(content)
            generated += 1
        except Exception as e:
            print(f"Error: {project_dir.name}: {e}", file=sys.stderr)
            errors += 1

    print(f"Generated: {generated}, Skipped: {skipped}, Errors: {errors}")


if __name__ == "__main__":
    main()

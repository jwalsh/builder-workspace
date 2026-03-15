#!/usr/bin/env bash
# health-check.sh — Validate bootstrap protocol health for builder-workspace
# Exit codes: 0 (ok), 1 (degraded), 2 (broken)
set -uo pipefail

HARD_PASS=0
HARD_FAIL=0
SOFT_PASS=0
SOFT_FAIL=0
RESULTS=()

check_hard() {
  local name="$1" cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then
    RESULTS+=("{\"check\":\"$name\",\"level\":\"hard\",\"status\":\"pass\"}")
    ((HARD_PASS++))
  else
    RESULTS+=("{\"check\":\"$name\",\"level\":\"hard\",\"status\":\"fail\"}")
    ((HARD_FAIL++))
  fi
}

check_soft() {
  local name="$1" cmd="$2"
  if eval "$cmd" >/dev/null 2>&1; then
    RESULTS+=("{\"check\":\"$name\",\"level\":\"soft\",\"status\":\"pass\"}")
    ((SOFT_PASS++))
  else
    RESULTS+=("{\"check\":\"$name\",\"level\":\"soft\",\"status\":\"warn\"}")
    ((SOFT_FAIL++))
  fi
}

# Hard checks
check_hard "git_repo" "git rev-parse --git-dir"
check_hard "projects_dir" "test -d projects"
check_hard "spec_files" "ls projects/*/spec.org >/dev/null 2>&1"
check_hard "claude_md_files" "ls projects/*/CLAUDE.md >/dev/null 2>&1"
check_hard "agents_md" "test -f AGENTS.md"
check_hard "cprr_store" "cprr list"
check_hard "git_remote" "git remote get-url origin"
check_hard "aq_home" "test -d ~/.aq"

# Soft checks
check_soft "bd_server" "bd list"
check_soft "bd_ready" "bd ready"
check_soft "sb_doctor" "sb doctor"
check_soft "aq_broadcasts" "aq status"
check_soft "aq_validate" "aq validate"

# Count projects
TOTAL_PROJECTS=$(ls -d projects/*/ 2>/dev/null | wc -l | tr -d ' ')
SPEC_COUNT=$(ls projects/*/spec.org 2>/dev/null | wc -l | tr -d ' ')
CLAUDE_COUNT=$(ls projects/*/CLAUDE.md 2>/dev/null | wc -l | tr -d ' ')
CONJ_COUNT=$(cprr list 2>/dev/null | wc -l | tr -d ' ')
ISSUE_COUNT=$(bd list 2>/dev/null | grep -c 'builder-workspace' || echo 0)
BROADCAST_COUNT=$(aq status --json 2>/dev/null | python3 -c "import json,sys; print(len(json.load(sys.stdin)))" 2>/dev/null || echo 0)

# Determine exit code
if [ "$HARD_FAIL" -gt 0 ]; then
  STATUS="broken"
  EXIT=2
elif [ "$SOFT_FAIL" -gt 0 ]; then
  STATUS="degraded"
  EXIT=1
else
  STATUS="ok"
  EXIT=0
fi

# Output JSON
cat <<ENDJSON
{
  "status": "$STATUS",
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "hard": {"pass": $HARD_PASS, "fail": $HARD_FAIL},
  "soft": {"pass": $SOFT_PASS, "fail": $SOFT_FAIL},
  "metrics": {
    "total_projects": $TOTAL_PROJECTS,
    "spec_org_files": $SPEC_COUNT,
    "claude_md_files": $CLAUDE_COUNT,
    "cprr_conjectures": $CONJ_COUNT,
    "bd_issues": $ISSUE_COUNT,
    "aq_broadcasts": $BROADCAST_COUNT
  },
  "checks": [$(IFS=,; echo "${RESULTS[*]}")]
}
ENDJSON

exit $EXIT

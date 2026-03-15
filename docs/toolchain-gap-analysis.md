# Toolchain Gap Analysis: aq / cprr / sb / bd

Generated 2026-03-15 from 5-team parallel agent sprint across 973 projects.

## Method

Five teams (ALPHA through ECHO) in isolated worktrees each pulled real
issues from `bd`, did work (scope docs, issue lifecycle), and documented
friction. Findings are cross-referenced across all 5 reports.

## What Works Well

| Pattern | Teams confirming |
|---------|-----------------|
| bd dependency chains advance on close | BRAVO, DELTA, ECHO |
| aq multi-file claims (comma-separated) | CHARLIE |
| bd label-based team filtering (`bd ready -l team-X`) | CHARLIE, all |
| aq file-based = offline-first, no network dependency | DELTA |
| bd rich filtering (title, label, status, priority, dates) | ALPHA, all |
| bd reopen for undo | DELTA |
| bd cycle detection on self-dependency | DELTA |
| cprr tag-based cross-project conjectures | CHARLIE |
| aq validate catches duplicate broadcasts (advisory) | DELTA |
| bd comments for durable handoff notes | ECHO |
| bd gate system for cross-rig waits | CHARLIE |

## Critical Gaps

### 1. No cross-tool linking

**Reported by**: BRAVO, ALPHA, ECHO, CHARLIE

- bd issues don't reference cprr conjecture IDs
- aq broadcasts don't reference bd issue IDs
- cprr conjectures don't reference bd issues
- Correlation requires string-matching project names across tools

**Fix**: `aq announce --issue <bd-id>`, `bd create --conjecture <cprr-id>`, `cprr add --issue <bd-id>`

### 2. Intra-worktree conflict blindness

**Reported by**: CHARLIE

- Two conjecture IDs from same worktree can claim the same file
- `aq check` only detects inter-worktree conflicts
- In monorepo or shared-worktree scenarios, no conflict detection at all

**Fix**: `aq check` should compare against ALL broadcasts, not just cross-worktree

### 3. Handoff context evaporates

**Reported by**: ECHO, BRAVO

- aq broadcasts expire (TTL 1hr default)
- bd issue descriptions are too thin ("Step 2 for X")
- `bd comments add` exists but nothing prompts agents to use it
- No structured handoff protocol in the default workflow

**Fix**: `bd close --comment "..."` or `bd handoff <closed> <next>` command

### 4. Issue titles are garbled

**Reported by**: ALPHA, BRAVO, ECHO

- Many titles are CLAUDE.md confirmation gate phrases: "You have read spec.org in this directory"
- Not meaningful work descriptions
- Agents can't triage from `bd ready` without reading spec.org

**Root cause**: `generate_claude_md.py` regex captures confirmation gate lines instead of build step descriptions

### 5. No team-scoped channels in aq

**Reported by**: CHARLIE

- All broadcasts global, no `--channel team-X`
- Signal-to-noise degrades at scale (57+ broadcasts visible to all)

**Fix**: `aq announce --channel team-charlie`, `aq status --channel team-charlie`

### 6. cprr validation gap

**Reported by**: DELTA

- Accepts empty titles and empty hypotheses
- No project-level filtering (`cprr list --project X`)
- No status filtering (`cprr list --status proven`)

### 7. bd has no `bd claim` / `bd start`

**Reported by**: ALPHA

- No state transition from open -> in_progress on claim
- Two agents can pull same issue without knowing
- `aq announce` fills this gap partially but isn't linked to bd

## Moderate Gaps

| Gap | Reported by |
|-----|-------------|
| No unified standup command | ECHO |
| `sb detect` doesn't exist (docs say it does) | three-primitive test |
| `sb list` MISPLACED semantics are opaque | ALPHA |
| `bd query` parser chokes on colons in labels | CHARLIE |
| No `aq revoke/cancel` (must wait for TTL) | DELTA |
| No retrospective tooling (proven/refuted filter) | ECHO |
| `bd remember` exists but nothing populates it | ECHO |
| No agent identity tracking per issue | ECHO |
| `aq announce` without `-f` succeeds silently | DELTA |
| bd `--json` output inconsistent across subcommands | ALPHA |

## Edge Case Results (Team DELTA probing)

| Test | Result |
|------|--------|
| `aq announce` no `-f` flag | Succeeds silently (should warn) |
| Duplicate conjecture ID broadcast | Succeeds, caught by `aq validate` |
| `bd dep X --blocks X` (self-dep) | Correctly errors: cycle detected |
| `cprr add ""` (empty title) | Succeeds (should reject) |
| `bd close` on already-closed | Idempotent (acceptable) |
| `bd close` on invalid ID | Clear error message |

## Highest-Value Improvements (ordered)

1. **Cross-tool linking** — `--issue` and `--conjecture` flags across aq/bd/cprr
2. **`bd close --comment`** — prompt for handoff context on close
3. **Fix issue title generation** — use actual build step names, not confirmation gate text
4. **`cprr list --project X`** — project-scoped conjecture views
5. **`aq --channel`** — team-scoped broadcasts
6. **`bd claim`/`bd start`** — explicit in-progress state transition linked to agent identity
7. **`bd standup`** — aggregate aq status + bd ready + cprr state for team label
8. **Intra-worktree conflict detection** in `aq check`
9. **cprr input validation** — reject empty titles
10. **`sb detect`** — implement the command that aq quickstart documents

## Team Sprint Results

| Team | Project worked | Step 1 closed | Step 2 unblocked | Scope doc | Conjectures |
|------|---------------|---------------|------------------|-----------|-------------|
| ALPHA | SemanticRFCSearch | No | N/A | Yes (worktree) | #3210 |
| BRAVO | WearablePetHealthMonitor | Yes | Yes | Yes | #3216 (confirmed) |
| CHARLIE | WaveEnergyConverter + VerticalWindTurbine | No | N/A | No | #3212 (cross-project) |
| DELTA | simulateurRisquesCyber | Yes | Yes | Yes | #3213 |
| ECHO | PeerLearningExchange | Yes | Yes | Yes (.org) | #3217 |

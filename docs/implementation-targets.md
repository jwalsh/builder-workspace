# Implementation Targets

30 projects selected for implementation across 3 stacks.

## Babashka (bb) — CLI Tools

Single-file Clojure scripts for code analysis, data processing, and developer tooling.
Run with `bb src/<name>.clj` or via `bb.edn` tasks.

| Project | Description | Complexity |
|---------|-------------|------------|
| AIDocumentationQualityChecker | Lint documentation for completeness, accuracy, consistency | Medium |
| CodeReadabilityAnalyzer | Score code readability, suggest improvements | Medium |
| CodePerformanceProfiler | Profile code, identify hotspots, suggest optimizations | Hard |
| DistributedLogAnalyzer | Parse/analyze logs from distributed systems, detect patterns | Medium |
| CodeExplanationGenerator | Generate line-by-line code explanations | Medium |
| AICodeStyleGuide | Enforce coding style rules across codebases | Easy |
| DeprecationDetective | Find deprecated APIs, libraries, patterns in codebases | Easy |
| CodeSmellDetector | Detect code smells, suggest refactoring | Medium |
| SecureCodeAnalyzer | Scan code for security vulnerabilities (OWASP patterns) | Hard |
| DataSyncIntegrityVerifier | Verify data integrity during sync operations | Medium |

### Quick start for any bb project
```bash
cd projects/<name>
cat > bb.edn << 'EOF'
{:tasks {run {:doc "Run the tool"
              :task (shell "bb src/main.clj" *command-line-args*)}
         test {:doc "Run tests"
               :task (shell "bb test/main_test.clj")}}}
EOF
mkdir -p src test
# Write src/main.clj with babashka.cli
```

## Bubble Tea TUI — Terminal Dashboards

Go applications with charmbracelet/bubbletea for interactive terminal UIs.
Build with `go build`, run with `./bin/<name>`.

| Project | Description | Complexity |
|---------|-------------|------------|
| MicroserviceHealthMonitor | Dashboard showing service health, latency, error rates | Hard |
| DistributedTaskScheduler | Interactive task queue viewer with job control | Hard |
| ThoughtPatternObserver | Visualize thought/decision patterns in terminal | Medium |
| SystemHealthScorer | Health score dashboard with drill-down | Medium |
| SmartCityOrchestrator | Multi-system urban dashboard | Hard |
| RealTimeSyncOrchestrator | Sync status across distributed systems | Medium |
| ZeroTrustOrchestrator | Security policy dashboard with live enforcement view | Hard |
| DesignPatternExplorer | Interactive design pattern catalog with examples | Easy |
| InteractiveKnowledgeExplorer | Tree-based knowledge navigation | Easy |
| WorkloadBalanceAnalyzer | Team workload visualization | Medium |

### Quick start for any TUI project
```bash
cd projects/<name>
go mod init github.com/jwalsh/<name>
go get github.com/charmbracelet/bubbletea
go get github.com/charmbracelet/lipgloss
go get github.com/charmbracelet/bubbles
# Write cmd/main.go with bubbletea.Program
```

## Replit — Web Applications

Python Flask/FastAPI web apps deployable on Replit's free tier.
Single `main.py` entry point, SQLite for persistence.

| Project | Description | Complexity |
|---------|-------------|------------|
| PairProgrammingSimulator | Web-based pair programming practice environment | Hard |
| ProgressiveCodeRefactorer | Interactive refactoring challenge platform | Medium |
| CodeDocumentationTrainer | Documentation writing exercises with scoring | Medium |
| SkillTreeExplorer | Visual skill tree with progress tracking | Easy |
| CareerMilestoneTracker | Simple CRUD for career milestone tracking | Easy |
| 3DHousingConfigurator | Web-based home design configurator | Hard |
| RemoteProductivityOptimizer | Productivity tips and workspace optimization | Easy |
| CodeSmellDetector | Web UI for code smell detection | Medium |
| SkillGrowthNavigator | Learning path recommendation engine | Medium |
| MicroservicesArchitectureTrainer | Interactive microservices learning platform | Medium |

### Quick start for any Replit project
```bash
cd projects/<name>
cat > main.py << 'EOF'
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
EOF
mkdir -p templates static data
cat > .replit << 'EOF'
run = "python main.py"
language = "python3"
EOF
```

## Priority Order

Start with the **Easy** projects in each category to validate the stack:

1. **bb**: DeprecationDetective, AICodeStyleGuide
2. **TUI**: DesignPatternExplorer, InteractiveKnowledgeExplorer
3. **Replit**: SkillTreeExplorer, CareerMilestoneTracker

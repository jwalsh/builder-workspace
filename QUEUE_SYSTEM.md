# Advanced Queue Processing System

## Overview

This system provides a sophisticated task queue with Redis backend and Claude Code agents running in tmux sessions for parallel task processing.

## Components

### 1. Advanced Queue System (`coordinator/advanced_queue.py`)
- **Priority-based task queue** with Redis backend
- **Task dependencies** support
- **Automatic retry logic** with exponential backoff
- **Agent worker pools** for parallel processing
- **Real-time monitoring** capabilities

Key features:
- 5 priority levels (CRITICAL, HIGH, NORMAL, LOW, DEFERRED)
- Task status tracking (QUEUED, ASSIGNED, IN_PROGRESS, COMPLETED, FAILED, RETRYING, CANCELLED)
- Dependency resolution before task execution
- Configurable retry limits

### 2. Claude Agent Sessions

Two tmux sessions running Claude Code with `--dangerously-skip-permissions`:
- `claude-agent-impl-1`: Implementation tasks
- `claude-agent-test-1`: Testing tasks

### 3. Queue Monitor (`coordinator/queue_status.py`)
Real-time dashboard showing:
- Queue sizes by type
- Task status distribution
- Recent task activity
- Agent status

## Setup Instructions

### Prerequisites
```bash
# Install tmux
brew install tmux

# Install Redis
brew install redis
brew services start redis

# Install Python dependencies
pip install aioredis rich
```

### Start the System

1. **Launch Redis** (if not already running):
```bash
redis-server
```

2. **Set up Claude agents**:
```bash
./setup_claude_agents.sh
```

This creates:
- Two Claude Code agent sessions
- Queue monitor dashboard
- Working directories for agents

3. **Submit tasks to the queue**:
```bash
# Submit example batch
./submit_task.py batch

# Submit individual tasks
./submit_task.py impl "Create user service" "services/user.py"
./submit_task.py test "Test user service" "tests/test_user.py"
```

## Working with Agents

### Monitor Sessions
```bash
# View queue status dashboard
tmux attach -t queue-monitor

# View implementation agent
tmux attach -t claude-agent-impl-1

# View testing agent
tmux attach -t claude-agent-test-1
```

### Send Commands to Agents
```bash
# Direct command to implementation agent
tmux send-keys -t claude-agent-impl-1 'implement the payment processing module' C-m

# Direct command to testing agent
tmux send-keys -t claude-agent-test-1 'write integration tests for the API' C-m
```

### Agent Workspaces
- Implementation: `agent-workspaces/implementation/`
- Testing: `agent-workspaces/testing/`

## Task Processing Flow

1. **Task Submission** → Redis queue with priority
2. **Agent Assignment** → Next available agent claims task
3. **Dependency Check** → Ensures prerequisites complete
4. **Processing** → Agent executes task
5. **Result Storage** → Output saved to Redis
6. **Status Update** → Dashboard reflects completion

## Queue Operations

### Python API
```python
from coordinator.advanced_queue import QueueTask, Priority, TaskQueue

async def example():
    queue = TaskQueue()
    await queue.connect()
    
    # Submit task
    task = QueueTask(
        task_type="implementation",
        payload={"description": "Build feature"},
        priority=Priority.HIGH
    )
    task_id = await queue.enqueue(task)
    
    # Check status
    stats = await queue.get_queue_stats()
    print(stats)
```

### CLI Tools
- `./submit_task.py` - Submit tasks
- `./coordinator/queue_status.py` - Monitor queues
- `./cleanup_agents.sh` - Clean up sessions

## Architecture

```
┌─────────────────────────────────────┐
│         Task Submission             │
│     (submit_task.py / API)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│          Redis Queue                │
│    (Priority-based, Persistent)     │
└──────────────┬──────────────────────┘
               │
      ┌────────┴────────┐
      ▼                 ▼
┌──────────┐     ┌──────────┐
│ Agent 1  │     │ Agent 2  │
│  (impl)  │     │  (test)  │
└──────────┘     └──────────┘
      │                 │
      ▼                 ▼
┌─────────────────────────────────────┐
│         Work Products               │
│    (Code, Tests, Documentation)     │
└─────────────────────────────────────┘
```

## Monitoring

The queue monitor dashboard (`tmux attach -t queue-monitor`) shows:
- **Pane 1**: Queue statistics
- **Pane 2**: Redis operations
- **Pane 3**: Task processor logs
- **Pane 4**: System metrics (htop)

## Cleanup

To stop all agents and clean up:
```bash
./cleanup_agents.sh
```

To stop Redis:
```bash
brew services stop redis
```

## Troubleshooting

### Redis Connection Issues
```bash
# Check Redis status
redis-cli ping

# Restart Redis
brew services restart redis
```

### Agent Not Processing
```bash
# Check agent session
tmux attach -t claude-agent-impl-1

# Restart agent
tmux kill-session -t claude-agent-impl-1
./setup_claude_agents.sh
```

### View Logs
```bash
# Queue logs
tail -f coordinator/logs/queue.log

# Redis monitor
redis-cli monitor
```
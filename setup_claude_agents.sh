#!/bin/bash
# setup_claude_agents.sh - Set up tmux sessions with Claude Code agents

# Configuration
SESSION_PREFIX="claude-agent"
WORKSPACE_DIR="$(pwd)"
QUEUE_MONITOR_SESSION="queue-monitor"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to check if tmux session exists
session_exists() {
    tmux has-session -t "$1" 2>/dev/null
}

# Function to create agent session
create_agent_session() {
    local session_name="$1"
    local agent_type="$2"
    local working_dir="$3"
    
    echo -e "${BLUE}Creating tmux session: ${session_name}${NC}"
    
    if session_exists "$session_name"; then
        echo -e "${YELLOW}Session ${session_name} already exists, skipping...${NC}"
        return
    fi
    
    # Create new tmux session
    tmux new-session -d -s "$session_name" -c "$working_dir"
    
    # Set up environment in the session
    tmux send-keys -t "$session_name" "cd $working_dir" C-m
    tmux send-keys -t "$session_name" "export AGENT_TYPE=$agent_type" C-m
    tmux send-keys -t "$session_name" "export AGENT_ID=$session_name" C-m
    
    # Start Claude Code with dangerous permissions flag
    tmux send-keys -t "$session_name" "claude --dangerously-skip-permissions" C-m
    
    echo -e "${GREEN}Session ${session_name} created successfully${NC}"
}

# Function to create queue monitor session
create_monitor_session() {
    local session_name="$1"
    
    echo -e "${BLUE}Creating queue monitor session: ${session_name}${NC}"
    
    if session_exists "$session_name"; then
        echo -e "${YELLOW}Session ${session_name} already exists, skipping...${NC}"
        return
    fi
    
    tmux new-session -d -s "$session_name" -c "$WORKSPACE_DIR"
    
    # Split window into panes for monitoring
    tmux split-window -h -t "$session_name"
    tmux split-window -v -t "$session_name:0.0"
    tmux split-window -v -t "$session_name:0.2"
    
    # Pane 0: Queue status monitor
    tmux send-keys -t "$session_name:0.0" "watch -n 2 'python3 -m coordinator.queue_status'" C-m
    
    # Pane 1: Redis monitor
    tmux send-keys -t "$session_name:0.1" "redis-cli monitor | grep -E 'queue:|task:'" C-m
    
    # Pane 2: Task processor logs
    tmux send-keys -t "$session_name:0.2" "tail -f coordinator/logs/queue.log" C-m
    
    # Pane 3: System metrics
    tmux send-keys -t "$session_name:0.3" "htop" C-m
    
    echo -e "${GREEN}Monitor session ${session_name} created successfully${NC}"
}

# Main setup
main() {
    echo -e "${BLUE}=== Setting up Claude Code Agent Sessions ===${NC}"
    echo -e "Workspace: $WORKSPACE_DIR"
    echo ""
    
    # Check if tmux is installed
    if ! command -v tmux &> /dev/null; then
        echo -e "${RED}Error: tmux is not installed${NC}"
        echo "Please install tmux first: brew install tmux"
        exit 1
    fi
    
    # Check if claude is installed
    if ! command -v claude &> /dev/null; then
        echo -e "${RED}Error: claude is not installed${NC}"
        echo "Please install Claude Code first"
        exit 1
    fi
    
    # Create working directories for agents
    mkdir -p "$WORKSPACE_DIR/agent-workspaces/implementation"
    mkdir -p "$WORKSPACE_DIR/agent-workspaces/testing"
    mkdir -p "$WORKSPACE_DIR/coordinator/logs"
    
    # Create agent sessions
    create_agent_session "${SESSION_PREFIX}-impl-1" "implementation" "$WORKSPACE_DIR/agent-workspaces/implementation"
    create_agent_session "${SESSION_PREFIX}-test-1" "testing" "$WORKSPACE_DIR/agent-workspaces/testing"
    
    # Create monitor session
    create_monitor_session "$QUEUE_MONITOR_SESSION"
    
    echo ""
    echo -e "${GREEN}=== Setup Complete ===${NC}"
    echo ""
    echo "Available tmux sessions:"
    tmux list-sessions
    echo ""
    echo -e "${BLUE}To attach to a session:${NC}"
    echo "  tmux attach -t ${SESSION_PREFIX}-impl-1    # Implementation agent"
    echo "  tmux attach -t ${SESSION_PREFIX}-test-1    # Testing agent"
    echo "  tmux attach -t ${QUEUE_MONITOR_SESSION}    # Queue monitor"
    echo ""
    echo -e "${BLUE}To send commands to agents:${NC}"
    echo "  tmux send-keys -t ${SESSION_PREFIX}-impl-1 'implement the authentication module' C-m"
    echo "  tmux send-keys -t ${SESSION_PREFIX}-test-1 'write tests for the auth module' C-m"
    echo ""
    echo -e "${BLUE}To kill all sessions:${NC}"
    echo "  ./cleanup_agents.sh"
}

# Run main function
main "$@"
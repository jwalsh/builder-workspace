#!/bin/bash
# cleanup_agents.sh - Clean up tmux sessions

# Configuration
SESSION_PREFIX="claude-agent"
QUEUE_MONITOR_SESSION="queue-monitor"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}Cleaning up Claude agent sessions...${NC}"

# Kill agent sessions
for session in $(tmux list-sessions -F "#{session_name}" 2>/dev/null | grep "^${SESSION_PREFIX}"); do
    echo -e "Killing session: ${session}"
    tmux kill-session -t "$session" 2>/dev/null
done

# Kill monitor session
if tmux has-session -t "$QUEUE_MONITOR_SESSION" 2>/dev/null; then
    echo -e "Killing monitor session: ${QUEUE_MONITOR_SESSION}"
    tmux kill-session -t "$QUEUE_MONITOR_SESSION"
fi

echo -e "${GREEN}Cleanup complete${NC}"

# Show remaining sessions
remaining=$(tmux list-sessions 2>/dev/null)
if [ -n "$remaining" ]; then
    echo -e "${YELLOW}Remaining tmux sessions:${NC}"
    echo "$remaining"
else
    echo "No tmux sessions remaining"
fi
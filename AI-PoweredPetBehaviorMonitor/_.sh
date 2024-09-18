#!/bin/bash

# Ensure script exits on any error
set -e

# Project directory
PROJECT_DIR=~/builder-workspace/AI-PoweredPetBehaviorMonitor

# RFC directory (relative to the project folder)
RFC_DIR="rfcs"

# Change to the project directory
cd "$PROJECT_DIR" || exit 1  # Exit with error if directory doesn't exist

# Create the RFC directory if it doesn't exist
mkdir -p "$RFC_DIR"

# Function to create an RFC file
create_rfc() {
    local id=$1
    local title=$2
    local description=$3
    local status=$4
    local assigned_to=$5
    local priority=$6
    local dependencies=$7
    local rfc_state=$8

    # RFC filename based on the ID
    local RFC_FILE="$RFC_DIR/rfc${id}.md"

    # RFC content (formatted as Markdown)
    local RFC_CONTENT=$(cat <<EOF
# RFC ${id}: ${title}

**Project:** AI-PoweredPetBehaviorMonitor
**Status:** ${status}
**Assigned to:** ${assigned_to}
**Priority:** ${priority}
**Dependencies:** ${dependencies}
**Task Type:** RFC
**RFC State:** ${rfc_state}

## Description

${description}
EOF
    )

    # Write RFC content to the file
    echo "$RFC_CONTENT" > "$RFC_FILE"

    echo "RFC ${id} created successfully at $RFC_FILE"
}

# Create the RFCs
create_rfc 6637 "Project Planning and Requirements Gathering" "Define project scope, goals, and requirements. Conduct research on pet behavior, AI techniques, and existing solutions. Gather input from stakeholders, such as pet owners, trainers, and veterinarians." "TODO" "project-manager" 5 "" "DRAFT"
create_rfc 6638 "System Architecture Design" "Design the overall system architecture, including components for data collection, AI model training, behavior analysis, recommendation generation, and data storage. Consider scalability, performance, security, and maintainability aspects." "TODO" "code-architect" 5 "\"Project Planning and Requirements Gathering\"" "REVIEW"
create_rfc 6642 "Database Design and Implementation" "Design and implement the database schema for storing pet behavior data, AI model parameters, user information, and related metadata. Consider scalability, performance, and security requirements." "TODO" "database-specialist" 3 "\"System Architecture Design\", \"Data Modeling and Requirements Analysis\"" "DRAFT"

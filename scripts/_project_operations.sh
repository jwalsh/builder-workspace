#!/bin/bash

# Coordinator Restructuring Script

# Set up error handling
set -e

# Define the base directory
BASE_DIR="coordinator"

# Create the new directory structure
mkdir -p $BASE_DIR/project_operations

# Create new files
touch $BASE_DIR/project_operations/__init__.py
touch $BASE_DIR/project_operations/decompose.py
touch $BASE_DIR/project_operations/rfc_processing.py
touch $BASE_DIR/project_operations/project_management.py
touch $BASE_DIR/project_operations/utils.py

# Function to extract content between specific lines
extract_content() {
    sed -n "/$2/,/$3/p" $1 | sed '1d;$d'
}

# Split the content of project_operations.py into new files
PROJECT_OPS_FILE="$BASE_DIR/project_operations.py"

# decompose.py
echo "import logging
from typing import List
from ..models import ProjectDefinition, Task, TaskType, RFCState
from ..llm import llm_manager
from ..prompts import AVAILABLE_AGENTS
from ..utils import extract_json_from_response

$(extract_content $PROJECT_OPS_FILE "async def decompose_project" "logging.info")" > $BASE_DIR/project_operations/decompose.py

# rfc_processing.py
echo "import logging
from typing import Optional
from ..models import Task, ProjectDefinition, TaskType, RFCState, ImplementationState
from ..db import update_task
from ..llm import llm_manager
from ..utils import extract_json_from_response

$(extract_content $PROJECT_OPS_FILE "async def process_rfc" "def parse_enum")

$(extract_content $PROJECT_OPS_FILE "def parse_enum" "def show_project_summary")" > $BASE_DIR/project_operations/rfc_processing.py

# project_management.py
echo "import asyncio
import logging
import sqlite3
from typing import List
from ..models import ProjectDefinition, Task, TaskType
from ..db import add_project_version, add_task, get_db_path, get_tasks, update_task
from ..utils import create_project_directory
from .decompose import decompose_project
from .rfc_processing import process_rfc

$(extract_content $PROJECT_OPS_FILE "def show_project_summary" "EOF")" > $BASE_DIR/project_operations/project_management.py

# Create __init__.py content
echo "from .decompose import decompose_project
from .rfc_processing import process_rfc
from .project_management import process_project, show_project_summary, show_project_tasks

__all__ = ['decompose_project', 'process_rfc', 'process_project', 'show_project_summary', 'show_project_tasks']" > $BASE_DIR/project_operations/__init__.py

# Rename the original file as a backup
mv $PROJECT_OPS_FILE ${PROJECT_OPS_FILE}.bak

echo "Restructuring complete. Please review the new files and update imports as necessary."

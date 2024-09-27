#!/bin/bash

mkdir -p coordinator/utils

if [ -f coordinator/utils.py ]; then
    mv coordinator/utils.py coordinator/utils.py.bak
    echo "Backed up coordinator/utils.py to coordinator/utils.py.bak"
fi

touch coordinator/utils/__init__.py
touch coordinator/utils/json_utils.py
touch coordinator/utils/file_utils.py
touch coordinator/utils/misc_utils.py

echo "Created utils directory and files"

cat << 'EOF' > coordinator/utils/__init__.py
from .json_utils import extract_json_from_response
from .file_utils import create_project_directory, sanitize_filename
from .misc_utils import (
    generate_cache_key,
    format_time_estimate,
    parse_dependencies,
    generate_task_id,
    calculate_project_progress,
    format_org_mode_task,
    generate_project_summary,
    validate_email,
    is_valid_url,
    truncate_string,
    format_file_size,
)
EOF

cat << 'EOF' > coordinator/utils/json_utils.py
import json
import re

def extract_json_from_response(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                return {}
        return {}
EOF

cat << 'EOF' > coordinator/utils/file_utils.py
import os
import json

def create_project_directory(project_name, description, tasks):
    # Implementation here
    pass

def sanitize_filename(filename):
    # Implementation here
    pass
EOF

cat << 'EOF' > coordinator/utils/misc_utils.py
import hashlib
import re
from datetime import datetime

def generate_cache_key(prompt, role):
    # Implementation here
    pass

def format_time_estimate(hours):
    # Implementation here
    pass

def parse_dependencies(dependencies_str):
    # Implementation here
    pass

def generate_task_id(project_id, title):
    # Implementation here
    pass

def calculate_project_progress(tasks):
    # Implementation here
    pass

def format_org_mode_task(task):
    # Implementation here
    pass

def generate_project_summary(project_name, description, tasks):
    # Implementation here
    pass

def validate_email(email):
    # Implementation here
    pass

def is_valid_url(url):
    # Implementation here
    pass

def truncate_string(string, max_length):
    # Implementation here
    pass

def format_file_size(size_in_bytes):
    # Implementation here
    pass
EOF

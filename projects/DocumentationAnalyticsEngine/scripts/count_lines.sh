#!/bin/bash
find . -type f -name "*.md" -or -name "*.py" -or -name "*.sh" | xargs wc -l

#!/bin/bash

# Ensure we're in the DocumentationAnalyticsEngine directory
cd "$(dirname "$0")"

# Function to create a directory if it doesn't exist
create_dir() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Created directory: $dir"
    fi
}

# Create additional directories
create_dir src/{backend,frontend,data_pipeline,analytics_engine,security,data,analytics,user,components}
create_dir docs
create_dir tests
create_dir deployment
create_dir rfcs

# Function to create a file
create_file() {
    local file=$1
    local dir=$(dirname "$file")
    create_dir "$dir"
    if [ ! -f "$file" ]; then
        touch "$file"
        echo "Created: $file"
    else
        echo "File already exists: $file"
    fi
}

# Read tasks.json and create files
jq -c '.[]' tasks.json | while read -r task; do
    id=$(echo $task | jq -r '.id')
    title=$(echo $task | jq -r '.title')
    task_type=$(echo $task | jq -r '.task_type')

    case $task_type in
        "rfc")
            create_file "rfcs/RFC_${id}_${title// /_}.md"
            ;;
        "decompose")
            create_file "src/${title// /_}.md"
            ;;
        "code_review")
            component=$(echo $title | awk '{print tolower($2)}')
            create_file "src/$component/${title// /_}.py"
            ;;
        "audit")
            case $title in
                "Test and Validate")
                    create_file "tests/test_${title// /_}.py"
                    ;;
                "Deploy and Monitor")
                    create_file "deployment/${title// /_}.sh"
                    ;;
                "Write Documentation")
                    create_file "docs/${title// /_}.md"
                    ;;
                "Implement Security Measures")
                    create_file "src/security/${title// /_}.py"
                    ;;
                *)
                    create_file "${title// /_}.txt"
                    ;;
            esac
            ;;
    esac
done

# Create helper scripts if they don't exist
create_file "update_repo.sh"
if [ ! -s "update_repo.sh" ]; then
    echo '#!/bin/bash
git add .
git commit -m "Update project structure"
git push origin main' > update_repo.sh
    chmod +x update_repo.sh
    echo "Updated content of: update_repo.sh"
fi

create_file "count_lines.sh"
if [ ! -s "count_lines.sh" ]; then
    echo '#!/bin/bash
find . -type f -name "*.md" -or -name "*.py" -or -name "*.sh" | xargs wc -l' > count_lines.sh
    chmod +x count_lines.sh
    echo "Updated content of: count_lines.sh"
fi

echo "Project structure and placeholder files have been updated."
echo "Helper scripts available: update_repo.sh and count_lines.sh"

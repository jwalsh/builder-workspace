for project_file in projects/*.txt; do
    # Read the project name from the filename (without .txt extension)
    project_name=$(basename "$project_file" .txt)

    # Read the project description from the file content
    project_description=$(cat "$project_file")

    # Create a project entry with the name and description
    echo  "$project_name: $project_description" 
    # python -m coordinator --name "$project_name"  --description "$project_description" --use-llm ollama
done

# sqlite3 tasks.db "SELECT id, project_id, title, status, assigned_to, task_type, rfc_state FROM tasks;" | tee tasks_output.txt

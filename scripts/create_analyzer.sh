#!/bin/bash

# Create main directory structure
mkdir -p analyzer/{analyzers,data,models,utils}

# Create __init__.py files
touch analyzer/__init__.py
touch analyzer/analyzers/__init__.py
touch analyzer/models/__init__.py
touch analyzer/utils/__init__.py

# Create main application files
cat << EOF > analyzer/__main__.py
from analyzer.cli import main

if __name__ == "__main__":
    main()
EOF

cat << EOF > analyzer/cli.py
import click
from analyzer.analyzers.category_analyzer import categorize_projects
from analyzer.analyzers.similarity_analyzer import analyze_project_similarity, analyze_category_similarity
from analyzer.analyzers.arxiv_analyzer import check_arxiv_papers
from analyzer.utils.file_operations import export_projects_to_csv, split_data_for_training
from analyzer.utils.text_processing import deduplicate_projects
from analyzer.models.category import show_categories

@click.command()
@click.option('--action', type=click.Choice(['categorize', 'analyze', 'categories', 'export', 'train-test', 'deduplicate', 'check-arxiv']), 
              default='categorize', 
              help='Action to perform')
@click.option('--max-refresh', type=int, default=3, help='Maximum number of times to refresh categories and re-run categorization.')
@click.option('--max-unknown', type=int, default=5, help='Maximum number of unknown categories to process during categorization.')
@click.option('--output-file', type=str, default='projects_for_training.csv', help='Output file name for CSV export.')
@click.option('--train-file', type=str, default='train_data.csv', help='Output file name for training data.')
@click.option('--test-file', type=str, default='test_data.csv', help='Output file name for test data.')
@click.option('--test-split', type=float, default=0.2, help='Proportion of data to use for testing (0.0 to 1.0).')
@click.option('--filename', type=str, default='PROJECTS.org', help='Input org file name.')
def main(action, max_refresh, max_unknown, output_file, train_file, test_file, test_split, filename):
    if action == 'categorize':
        categorize_projects(max_refresh, max_unknown, filename)
    elif action == 'analyze':
        analyze_project_similarity(filename)
        analyze_category_similarity()
    elif action == 'categories':
        show_categories()
    elif action == 'export':
        export_projects_to_csv(output_file, filename)
    elif action == 'train-test':
        export_projects_to_csv(output_file, filename)
        split_data_for_training(output_file, train_file, test_file, test_split)
    elif action == 'deduplicate':
        deduplicate_projects(filename)
    elif action == 'check-arxiv':
        check_arxiv_papers(filename)

if __name__ == '__main__':
    main()
EOF

# Create analyzer files
cat << EOF > analyzer/analyzers/__init__.py
from .category_analyzer import categorize_projects
from .similarity_analyzer import analyze_project_similarity, analyze_category_similarity
from .arxiv_analyzer import check_arxiv_papers
EOF

# ... (rest of the file content remains the same)

# Update requirements.txt
cat << EOF > requirements.txt
beautifulsoup4==4.12.2
click==8.1.3
google-generativeai==0.4.0
matplotlib==3.7.1
numpy==1.24.3
orgparse==0.4.20231004
requests==2.31.0
scikit-learn==1.2.2
scipy==1.12.0
EOF

echo "Analyzer module setup complete. Please review the files and install the required packages using 'pip install -r requirements.txt'."

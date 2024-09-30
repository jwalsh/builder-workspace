#!/usr/bin/env python3

import json
import os
from typing import Dict, List, Optional
from itertools import chain
from functools import lru_cache

import click

# List of featured projects (keep the same as before)

FEATURED_PROJECTS = [
    "AI-PoweredPetBehaviorMonitor",
    "AICodeReviewer",
    "AIDocumentationAssistant",
    "AISecurityAuditor",
    "AITravelItineraryPlanner",
    "AdFlow",
    "AugmentedRealityEducation",
    "BionicProsthesisNerve",
    "BlockchainSupplyChainTracker",
    "BuilderAgents",
    "CodeLibra",
    "CyberAttackPredictor",
    "DocumentationAnalyticsEngine",
    "MultilinguaStoryForge",
    "NeuralNetworkTrainer",
    "PersonalizedAIHealthCoach",
    "PredictiveMaintenanceForHomes",
    "QuantumComputingSimulator",
    "RealTimeAnalyticsEngine",
    "RealTimeLanguageTranslator",
    "SmartCityOrchestrator",
    "SmartContractAnalyzer",
    "VirtualFittingRoom",
]

@lru_cache(maxsize=None)
def load_json_file(file_path: str) -> Dict:
    """Load and return JSON data from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        click.echo(f"Warning: File not found - {file_path}", err=True)
        return {}
    except json.JSONDecodeError:
        click.echo(f"Error: Invalid JSON in file - {file_path}", err=True)
        return {}

def find_json_file(project_dir: str, filename: str) -> Optional[str]:
    """Find JSON file in project root or config directory."""
    root_path = os.path.join(project_dir, filename)
    config_path = os.path.join(project_dir, "config", filename)
    
    if os.path.exists(root_path):
        return root_path
    elif os.path.exists(config_path):
        return config_path
    else:
        return None

def get_project_state(project_name: str) -> Dict:
    """Get the current state of a project."""
    project_dir = os.path.join("projects", project_name)
    
    project_info_path = find_json_file(project_dir, "project_info.json")
    tasks_path = find_json_file(project_dir, "tasks.json")
    
    if not project_info_path or not tasks_path:
        click.echo(f"Error: Required JSON files not found for project {project_name}", err=True)
        return {
            "name": project_name,
            "description": "Error: Required JSON files not found",
            "total_tasks": 0,
            "completed_tasks": 0,
            "progress": "N/A",
            "top_tasks": []
        }
    
    project_info = load_json_file(project_info_path)
    tasks = load_json_file(tasks_path)

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.get('status') == 'COMPLETED')
    
    # Sort tasks by priority (assuming lower number means higher priority)
    sorted_tasks = sorted(tasks, key=lambda x: x.get('priority', float('inf')))
    top_tasks = [
        {
            "title": task.get('title', 'Untitled'),
            "priority": task.get('priority', 'N/A'),
            "status": task.get('status', 'UNKNOWN')
        }
        for task in sorted_tasks[:3]  # Get top 3 tasks
    ]
    
    return {
        "name": project_name,
        "description": project_info.get('description', 'No description available'),
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress": f"{(completed_tasks / total_tasks) * 100:.2f}%" if total_tasks > 0 else "N/A",
        "top_tasks": top_tasks
    }

def print_project_state(project_state: Dict):
    """Print the state of a project in a formatted manner."""
    click.echo(f"\nProject: {project_state['name']}")
    click.echo(f"Description: {project_state['description']}")
    click.echo(f"Total Tasks: {project_state['total_tasks']}")
    click.echo(f"Completed Tasks: {project_state['completed_tasks']}")
    click.echo(f"Progress: {project_state['progress']}")
    click.echo("Top Priority Tasks:")
    for task in project_state['top_tasks']:
        click.echo(f"  - {task['title']} (Priority: {task['priority']}, Status: {task['status']})")
    click.echo("-" * 50)

@click.command()
@click.option('--project', help='Specify a single project to check')
@click.option('--all', 'check_all', is_flag=True, help='Check all projects, including non-featured ones')
def main(project: str, check_all: bool):
    """Get current state of projects in Builder Workspace."""
    if project:
        if project not in FEATURED_PROJECTS and not check_all:
            click.echo(f"Error: {project} is not a recognized featured project", err=True)
            return
        projects_to_check = [project]
    elif check_all:
        projects_to_check = [d for d in os.listdir("projects") if os.path.isdir(os.path.join("projects", d))]
    else:
        projects_to_check = FEATURED_PROJECTS

    project_states = map(get_project_state, projects_to_check)
    
    # Sort projects by progress (completed tasks / total tasks)
    sorted_states = sorted(
        project_states, 
        key=lambda x: x['completed_tasks'] / x['total_tasks'] if x['total_tasks'] > 0 else 0, 
        reverse=True
    )

    for project_state in sorted_states:
        print_project_state(project_state)

    if check_all:
        total_projects = len(projects_to_check)
        total_tasks = sum(state['total_tasks'] for state in sorted_states)
        total_completed = sum(state['completed_tasks'] for state in sorted_states)
        overall_progress = f"{(total_completed / total_tasks) * 100:.2f}%" if total_tasks > 0 else "N/A"
        
        click.echo(f"\nOverall Workspace Summary:")
        click.echo(f"Total Projects: {total_projects}")
        click.echo(f"Total Tasks: {total_tasks}")
        click.echo(f"Total Completed Tasks: {total_completed}")
        click.echo(f"Overall Progress: {overall_progress}")

if __name__ == "__main__":
    main()

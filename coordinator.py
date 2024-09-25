import json
import logging
import os
import random
import re
import sqlite3
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional

import anthropic
import click
import requests
from pydantic import BaseModel, Field

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TaskType(str, Enum):
    RFC = "rfc"
    DECOMPOSE = "decompose"
    RFC_REVIEW = "rfc_review"
    CODE_REVIEW = "code_review"
    AUDIT = "audit"
    UNKNOWN = "unknown"


class RFCState(str, Enum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    REVIEW = "REVIEW"
    REVISE = "REVISE"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    DEFERRED = "DEFERRED"
    WITHDRAWN = "WITHDRAWN"
    IMPLEMENTING = "IMPLEMENTING"
    IMPLEMENTED = "IMPLEMENTED"
    OBSOLETE = "OBSOLETE"
    UNKNOWN = "UNKNOWN"


class LLMProvider(str, Enum):
    OLLAMA = "ollama"
    CLAUDE = "claude"
    RANDOM = "random"


class ProjectDefinition(BaseModel):
    name: str
    description: str


class Task(BaseModel):
    id: int
    project_id: str
    title: str
    description: str
    status: str
    assigned_to: str
    priority: int
    dependencies: List[str]
    task_type: TaskType = Field(default=TaskType.UNKNOWN)
    rfc_state: Optional[RFCState] = Field(default=None)


class LLMConfig(BaseModel):
    provider: LLMProvider
    ollama_healthy: bool
    claude_healthy: bool
    last_check: datetime  # Change this from str to datetime


# Initialize Anthropic client
client = anthropic.Client(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Global configuration
config: LLMConfig = None

# Config file path
CONFIG_FILE = "llm_config.json"

COORDINATOR_PROMPT = """You are an AI Project Coordinator named Coordinator. Your primary responsibilities include: 1. Generating Request for Comments (RFCs) documents, 2. Creating project plans and coordination documents, 3. Facilitating communication between team members, 4. Establishing processes for efficient collaboration, 5. Ensuring projects stay on track, 6. Performing initial triage and assignment of tasks."""
# Inlined system prompts for each role
SYSTEM_PROMPTS = {
    "coordinator": COORDINATOR_PROMPT,
    "default": COORDINATOR_PROMPT,
    "backend-developer": """You are an AI assistant specializing in back-end software development project management. Your responsibilities include understanding the problem requirements, designing and implementing efficient solutions, writing clean and well-documented code, testing thoroughly, providing clear explanations, and adhering to best practices for each language.""",
    "code-architect": """You are a code architect AI assistant specializing in software development project management. Your responsibilities include understanding project requirements, designing the overall architecture, breaking down the problem into manageable tasks, providing guidance on best practices, reviewing code, ensuring adherence to standards, and coordinating with other stakeholders. Focus on maintainability, modularity, scalability, and consider edge cases, error handling, and performance optimizations.""",
    "database-specialist": """You are an AI assistant specializing in database design and implementation for software projects. Your role is to provide expertise on database-related tasks, such as data modeling, schema design, query optimization, and performance tuning. You should be familiar with various database management systems and their query languages. Analyze requirements, propose appropriate database solutions, and assist in implementing and optimizing database components.""",
    "devops-engineer": """You are a DevOps engineer specializing in implementing code and infrastructure. Your role is to provide efficient and well-documented solutions, ensuring code quality, maintainability, and adherence to best practices. Your responsibilities include understanding requirements, implementing solutions in requested languages, writing clean code, following best practices, providing explanations, suggesting improvements, addressing edge cases, and providing deployment instructions.""",
    "frontend-developer": """You are a frontend developer agent specializing in web development. Your responsibilities include writing clean, efficient, and well-documented code, following best practices, providing clear explanations and comments, testing thoroughly, and collaborating with team members. Strive to produce high-quality, maintainable, and efficient solutions while adhering to project requirements and coding best practices.""",
    "project-manager": """You are an AI project manager specializing in software development projects. Your role is to oversee and manage the development of the project. Your responsibilities include defining project goals and scope, creating a project plan, assigning tasks, monitoring progress, mitigating risks, facilitating communication, ensuring code quality, providing guidance, and reporting project status. You should have a strong understanding of software development methodologies, project management principles, and programming concepts.""",
    "qa-tester": """You are a QA tester agent specializing in testing software implementations. Your role is to thoroughly test and validate implementations. Your responsibilities include understanding requirements, designing comprehensive test cases, writing test scripts, executing tests, analyzing results, reporting issues, and providing feedback for improvement. Ensure that the implementations are thoroughly tested, reliable, and meet project requirements.""",
    "security-specialist": """You are a security-specialist AI assistant focused on ensuring secure implementation of software projects. Your role is to review the code, identify potential security vulnerabilities, and provide recommendations for secure coding practices. You should have expertise in secure coding principles, common security risks, and best practices for mitigating those risks.""",
    "task-decomposer": """You are a task decomposition AI assistant specialized in software development project management. Your role is to break down complex projects into smaller, manageable tasks and subtasks. You will receive a project definition and create a structured task list with clear descriptions and dependencies. Consider all aspects of the project, including requirements gathering, design, implementation, testing, and deployment. Your output should be a well-organized task list suitable for project management tools.""",
    "technical-writer": """You are a highly skilled technical writer specializing in software development documentation. Your role is to create clear, concise, and well-structured documentation for software projects. Your responsibilities include understanding the problem, writing comprehensive documentation covering problem statement, algorithm explanation, implementation details, code examples, testing procedures, and potential optimizations. Ensure the documentation is well-organized, easy to follow, and suitable for both novice and experienced developers. Maintain a professional tone and adhere to best practices in technical writing.""",
}

AVAILABLE_AGENTS = [
    "backend-developer",
    "code-architect",
    "database-specialist",
    "devops-engineer",
    "frontend-developer",
    "project-manager",
    "qa-tester",
    "security-specialist",
    "task-decomposer",
    "technical-writer",
]


def get_db_path():
    return os.path.join(os.getcwd(), "tasks.db")


def load_config():
    global config
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config_data = json.load(f)
            config_data["last_check"] = datetime.fromisoformat(
                config_data["last_check"]
            )
            config = LLMConfig(**config_data)
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            logging.warning("Invalid config file. Creating a new configuration.")
            create_default_config()
    else:
        create_default_config()


def create_default_config():
    global config
    config = LLMConfig(
        provider=LLMProvider.OLLAMA,
        ollama_healthy=True,
        claude_healthy=True,
        last_check=datetime.now(),
    )
    save_config()


def save_config():
    config_dict = config.dict()
    config_dict["last_check"] = config.last_check.isoformat()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_dict, f)


def update_health_status(force_check=False):
    global config
    if force_check or (
        datetime.now() - datetime.fromisoformat(config.last_check)
    ) > timedelta(hours=4):
        config.ollama_healthy = check_ollama_health()
        config.claude_healthy = check_claude_health()
        config.last_check = datetime.now()
        save_config()


def check_ollama_health():
    try:
        response = requests.get("http://localhost:11434/api/version")
        return response.status_code == 200
    except requests.RequestException:
        return False


def check_claude_health():
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hello"}],
        )
        return True
    except Exception:
        return False


def update_health_status(force_check=False):
    global config
    if force_check or (datetime.now() - config.last_check) > timedelta(hours=4):
        config.ollama_healthy = check_ollama_health()
        config.claude_healthy = check_claude_health()
        config.last_check = datetime.now()
        save_config()


def get_active_provider():
    update_health_status()
    if config.provider == LLMProvider.RANDOM:
        available_providers = []
        if config.ollama_healthy:
            available_providers.append(LLMProvider.OLLAMA)
        if config.claude_healthy:
            available_providers.append(LLMProvider.CLAUDE)
        return random.choice(available_providers) if available_providers else None
    elif config.provider == LLMProvider.OLLAMA and config.ollama_healthy:
        return LLMProvider.OLLAMA
    elif config.provider == LLMProvider.CLAUDE and config.claude_healthy:
        return LLMProvider.CLAUDE
    else:
        return None


def run_llm_command(prompt: str, cache_key: str, role: str) -> Optional[str]:
    provider = get_active_provider()
    if provider == LLMProvider.OLLAMA:
        return run_ollama_command(prompt, cache_key, role)
    elif provider == LLMProvider.CLAUDE:
        return run_claude_command(prompt, cache_key, role)
    else:
        logging.error("No healthy LLM provider available")
        return None


def run_ollama_command(prompt: str, cache_key: str, role: str) -> Optional[str]:
    system_message = (
        f"Cache key: {cache_key}\n{SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS['default'])}"
    )
    logging.info(f"{role}: {cache_key}")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:latest",
                "prompt": f"{system_message}\n\n{prompt}",
            },
        )
        response.raise_for_status()
        return response.json().get("response")
    except requests.RequestException as e:
        logging.error(f"Error calling Ollama API: {e}")
        return None


def run_claude_command(prompt: str, cache_key: str, role: str) -> Optional[str]:
    system_message = (
        f"Cache key: {cache_key}\n{SYSTEM_PROMPTS.get(role, SYSTEM_PROMPTS['default'])}"
    )
    try:
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=2000,
            temperature=0.5,
            system=system_message,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        logging.error(f"Error calling Claude API: {e}")
        return None


def create_tables():
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS tasks
                     (id INTEGER PRIMARY KEY,
                      project_id TEXT,
                      title TEXT,
                      description TEXT,
                      status TEXT,
                      assigned_to TEXT,
                      priority INTEGER,
                      dependencies TEXT,
                      task_type TEXT,
                      rfc_state TEXT)"""
        )
        c.execute(
            """CREATE TABLE IF NOT EXISTS project_versions
                     (id TEXT PRIMARY KEY,
                      definition TEXT,
                      created_at TIMESTAMP)"""
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")
    finally:
        conn.close()


def add_project_version(project_id: str, definition: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """INSERT OR REPLACE INTO project_versions (id, definition, created_at)
                     VALUES (?, ?, ?)""",
            (project_id, definition, datetime.utcnow().isoformat()),
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error adding project version: {e}")
    finally:
        conn.close()


def add_task(task: Task):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """INSERT INTO tasks (project_id, title, description, status, assigned_to, priority, dependencies, task_type, rfc_state)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                task.project_id,
                task.title,
                task.description,
                task.status,
                task.assigned_to,
                task.priority,
                json.dumps(task.dependencies),
                task.task_type.value,
                task.rfc_state.value if task.rfc_state else None,
            ),
        )
        task_id = c.lastrowid
        conn.commit()
        return task_id
    except sqlite3.Error as e:
        logging.error(f"Error adding task: {e}")
        return None
    finally:
        conn.close()


def get_tasks(project_id: str) -> List[Task]:
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,))
        tasks = c.fetchall()
        return [
            Task(
                id=task[0],
                project_id=task[1],
                title=task[2],
                description=task[3],
                status=task[4],
                assigned_to=task[5],
                priority=task[6],
                dependencies=json.loads(task[7]),
                task_type=TaskType(task[8]),
                rfc_state=RFCState(task[9]) if task[9] else None,
            )
            for task in tasks
        ]
    except sqlite3.Error as e:
        logging.error(f"Error getting tasks: {e}")
        return []
    finally:
        conn.close()


def update_task(task: Task):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """UPDATE tasks SET
                     title = ?, description = ?, status = ?, assigned_to = ?,
                     priority = ?, dependencies = ?, task_type = ?, rfc_state = ?
                     WHERE id = ?""",
            (
                task.title,
                task.description,
                task.status,
                task.assigned_to,
                task.priority,
                json.dumps(task.dependencies),
                task.task_type.value,
                task.rfc_state.value if task.rfc_state else None,
                task.id,
            ),
        )
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error updating task: {e}")
    finally:
        conn.close()


def extract_json_from_response(text: str) -> Dict[str, Any]:
    try:
        # First, try to parse the entire text as JSON
        return json.loads(text)
    except json.JSONDecodeError:
        # If that fails, look for JSON-like content
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(0))
            except json.JSONDecodeError:
                logging.error("Failed to extract valid JSON from the response")
                return {}
        else:
            logging.error("No JSON-like content found in the response")
            return {}


def decompose_project(project_definition: ProjectDefinition) -> List[Task]:
    prompt = f"""Decompose the following project into initial high-level tasks:

Project Name: {project_definition.name}
Description: {project_definition.description}

Please provide a JSON array of tasks, where each task has the following structure:
{{
  "title": "Task title",
  "description": "Task description",
  "status": "TODO",
  "assigned_to": "Agent type (must be one of: {', '.join(AVAILABLE_AGENTS)})",
  "priority": 1-5 (1 being highest priority),
  "dependencies": ["Dependency task title", "Another dependency"],
  "task_type": "One of: rfc, decompose, rfc_review, code_review, audit",
  "rfc_state": "DRAFT (only if task_type is rfc, otherwise null)"
}}"""

    cache_key = f"decompose_project_{project_definition.name}"
    tasks_response = run_llm_command(prompt, cache_key, "task-decomposer")

    if not tasks_response:
        logging.error("No response received from LLM")
        return []

    tasks_data = extract_json_from_response(tasks_response)

    if not isinstance(tasks_data, list):
        logging.error("Invalid response format: expected a list of tasks")
        return []

    tasks = []
    for task in tasks_data:
        try:
            task_type = TaskType(task.get("task_type", "unknown").lower())
        except ValueError:
            task_type = TaskType.UNKNOWN

        rfc_state = None
        if task_type == TaskType.RFC:
            try:
                rfc_state = RFCState(task.get("rfc_state", "UNKNOWN").upper())
            except ValueError:
                rfc_state = RFCState.UNKNOWN

        # Ensure assigned_to is in the list of available agents
        if task["assigned_to"] not in AVAILABLE_AGENTS:
            task["assigned_to"] = (
                "project-manager"  # Default to project manager if invalid
            )

        tasks.append(
            Task(
                id=0,
                project_id=project_definition.name,
                title=task["title"],
                description=task["description"],
                status=task["status"],
                assigned_to=task["assigned_to"],
                priority=task["priority"],
                dependencies=task["dependencies"],
                task_type=task_type,
                rfc_state=rfc_state,
            )
        )

    return tasks


def process_rfc(task: Task, project_definition: ProjectDefinition) -> Task:
    prompt = f"""Review and update the following RFC task:

Project Name: {project_definition.name}
Description: {project_definition.description}

Task:
{task.model_dump_json(indent=2)}

Please review the RFC and suggest any necessary changes or improvements. If the RFC is ready for the next state, update the rfc_state field accordingly. Provide your response as a JSON object with the updated task fields. Ensure that the 'assigned_to' field is one of the following: {', '.join(AVAILABLE_AGENTS)}"""

    cache_key = (
        f"process_rfc_{task.id}_{task.rfc_state.value if task.rfc_state else 'UNKNOWN'}"
    )
    updated_task_response = run_llm_command(prompt, cache_key, "code-architect")

    if not updated_task_response:
        logging.error(f"No response received from LLM for task {task.id}")
        return task

    updated_task_data = extract_json_from_response(updated_task_response)

    if not updated_task_data:
        logging.error(f"Failed to extract valid JSON for task {task.id}")
        return task

    # Ensure assigned_to is in the list of available agents
    if updated_task_data.get("assigned_to") not in AVAILABLE_AGENTS:
        updated_task_data["assigned_to"] = (
            task.assigned_to
        )  # Keep the original assignment

    try:
        updated_task_data["task_type"] = TaskType(
            updated_task_data.get("task_type", "unknown").lower()
        )
    except ValueError:
        updated_task_data["task_type"] = TaskType.UNKNOWN

    if updated_task_data["task_type"] == TaskType.RFC:
        try:
            updated_task_data["rfc_state"] = RFCState(
                updated_task_data.get("rfc_state", "UNKNOWN").upper()
            )
        except ValueError:
            updated_task_data["rfc_state"] = RFCState.UNKNOWN
    else:
        updated_task_data["rfc_state"] = None

    return Task(**updated_task_data)


def show_project_summary():
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """
            SELECT project_id, COUNT(*) as task_count
            FROM tasks
            GROUP BY project_id
            ORDER BY project_id
        """
        )
        projects = c.fetchall()
        click.echo("Projects and task counts:")
        for project, count in projects:
            click.echo(f"{project}: {count} tasks")
    except sqlite3.Error as e:
        logging.error(f"Error showing project summary: {e}")
    finally:
        conn.close()


def show_project_tasks(project_name: str):
    try:
        conn = sqlite3.connect(get_db_path())
        c = conn.cursor()
        c.execute(
            """
            SELECT id, priority, title, status, assigned_to, task_type, rfc_state
            FROM tasks
            WHERE project_id = ?
            ORDER BY id
        """,
            (project_name,),
        )
        tasks = c.fetchall()

        if not tasks:
            click.echo(
                f"Warning: No tasks found for project '{project_name}'. The project may not have been decomposed yet."
            )
            return

        click.echo(f"Tasks for project '{project_name}':")
        for task in tasks:
            click.echo(
                f"ID: {task[0]}, Priority: {task[1]}, Title: {task[2]}, Status: {task[3]}, Assigned: {task[4]}, Type: {task[5]}, RFC State: {task[6]}"
            )
    except sqlite3.Error as e:
        logging.error(f"Error showing project tasks: {e}")
    finally:
        conn.close()


def create_project_directory(project_name: str, description: str, tasks: List[Task]):
    projects_dir = os.path.join(os.getcwd(), "projects")
    if not os.path.exists(projects_dir):
        os.makedirs(projects_dir)

    project_path = os.path.join(projects_dir, project_name)

    try:
        if not os.path.exists(project_path):
            os.makedirs(project_path)

        # Create a project info file
        with open(os.path.join(project_path, "project_info.json"), "w") as f:
            json.dump({"name": project_name, "description": description}, f, indent=2)

        # Create a tasks file
        with open(os.path.join(project_path, "tasks.json"), "w") as f:
            json.dump([task.dict() for task in tasks], f, indent=2)

        click.echo(f"Project directory created at: {project_path}")
    except OSError as e:
        logging.error(f"Error creating project directory: {e}")


def process_project(name: str, description: str, force: bool):
    try:
        project_definition = ProjectDefinition(name=name, description=description)

        add_project_version(project_definition.name, project_definition.json())

        existing_tasks = get_tasks(project_definition.name)

        if not existing_tasks or force:
            if existing_tasks and force:
                click.echo(
                    f"\nForce flag used. Re-decomposing project '{project_definition.name}' into tasks..."
                )
                # You might want to add logic here to remove existing tasks if necessary
            else:
                click.echo("\nDecomposing project into tasks...")

            initial_tasks = decompose_project(project_definition)
            for task in initial_tasks:
                task_id = add_task(task)
                if task_id:
                    task.id = task_id
                    click.echo(
                        f"Added task: {task.title} (Type: {task.task_type}, Assigned to: {task.assigned_to})"
                    )
                else:
                    logging.error(f"Failed to add task: {task.title}")

            # Create project directory after decomposition
            create_project_directory(
                project_definition.name, project_definition.description, initial_tasks
            )
        else:
            click.echo(
                f"\nTasks already exist for project '{project_definition.name}'. Skipping decomposition. Use --force to override."
            )

            # Create project directory with existing tasks
            create_project_directory(
                project_definition.name, project_definition.description, existing_tasks
            )

        click.echo("\nProcessing RFC tasks...")
        rfc_tasks = [
            task
            for task in get_tasks(project_definition.name)
            if task.task_type == TaskType.RFC
        ]
        for rfc_task in rfc_tasks:
            try:
                updated_rfc_task = process_rfc(rfc_task, project_definition)
                update_task(updated_rfc_task)
                click.echo(
                    f"Processed RFC task: {updated_rfc_task.title} (New state: {updated_rfc_task.rfc_state})"
                )
            except Exception as e:
                logging.error(f"Error processing RFC task {rfc_task.id}: {str(e)}")

        click.echo(
            "\nProject setup complete. Tasks added to the database and project directory created."
        )
    except Exception as e:
        logging.error(f"An error occurred while processing the project: {str(e)}")
        raise


@click.command()
@click.option("--name", help="Project name")
@click.option("--description", help="Project description")
@click.option(
    "--force", is_flag=True, help="Force task decomposition even if tasks already exist"
)
@click.option("--list", is_flag=True, help="List all projects and their task counts")
@click.option(
    "--use-llm",
    type=click.Choice(["ollama", "claude", "random"]),
    default="ollama",
    help="Choose LLM provider",
)
@click.option(
    "--check-health", is_flag=True, help="Check health status of LLM providers"
)
@click.option(
    "--reset-config", is_flag=True, help="Reset the configuration to default values"
)
def main(
    name: str,
    description: str,
    force: bool,
    list: bool,
    use_llm: str,
    check_health: bool,
    reset_config: bool,
):
    try:
        if reset_config:
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            click.echo("Configuration has been reset.")

        load_config()

        if check_health:
            update_health_status(force_check=True)
            click.echo(
                f"Ollama health: {'Healthy' if config.ollama_healthy else 'Unhealthy'}"
            )
            click.echo(
                f"Claude health: {'Healthy' if config.claude_healthy else 'Unhealthy'}"
            )
            return

        config.provider = LLMProvider(use_llm)
        save_config()

        create_tables()

        if list:
            show_project_summary()
        elif name:
            if force:
                # If force flag is used without a description, fetch the existing description
                if not description:
                    conn = sqlite3.connect(get_db_path())
                    c = conn.cursor()
                    c.execute(
                        "SELECT definition FROM project_versions WHERE id = ?", (name,)
                    )
                    result = c.fetchone()
                    conn.close()

                    if result:
                        try:
                            existing_project = json.loads(result[0])
                            description = existing_project.get(
                                "description", "No description available"
                            )
                        except json.JSONDecodeError:
                            click.echo(
                                f"Error: Invalid JSON data for project '{name}'. Please provide a description."
                            )
                            return
                    else:
                        click.echo(
                            f"Error: No existing project found with name '{name}'. Please provide a description."
                        )
                        return

            if description or force:
                process_project(name, description, force)
            else:
                show_project_tasks(name)
        else:
            click.echo(
                "Please provide a project name or use --list to see all projects."
            )
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        click.echo("An error occurred. Please check the logs for more information.")


if __name__ == "__main__":
    main()

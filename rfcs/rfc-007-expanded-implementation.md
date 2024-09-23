# Expanded Coordinator Implementation Plan

## 1. Update Task Types and Workflows

First, we need to update our task types and workflow to include implementation stages:

```python
# coordinator/models.py

class TaskType(str, Enum):
    RFC = "rfc"
    IMPLEMENTATION = "implementation"
    CODE_REVIEW = "code_review"
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    INFRASTRUCTURE = "infrastructure"
    MONITORING = "monitoring"
    DIAGRAM = "diagram"

class ImplementationState(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    TESTING = "testing"
    COMPLETED = "completed"

class Task(BaseModel):
    # ... existing fields ...
    implementation_state: Optional[ImplementationState] = None
```

## 2. Expand Agent Roles

Create new agent roles for different aspects of implementation:

```python
# coordinator/prompts.py

SYSTEM_PROMPTS = {
    # ... existing prompts ...
    "implementation_developer": """You are an Implementation Developer AI responsible for translating approved RFCs into actual code. Your tasks include:
1. Analyzing the approved RFC
2. Writing clean, efficient, and well-documented code
3. Following best practices and coding standards
4. Implementing unit tests for the code
5. Providing clear comments and documentation within the code""",
    
    "infrastructure_engineer": """You are an Infrastructure Engineer AI tasked with setting up and managing the infrastructure for the project. Your responsibilities include:
1. Designing infrastructure architecture based on project requirements
2. Creating Infrastructure as Code (IaC) scripts (e.g., Terraform, CloudFormation)
3. Setting up CI/CD pipelines
4. Ensuring scalability and reliability of the infrastructure
5. Implementing security best practices""",
    
    "monitoring_specialist": """You are a Monitoring Specialist AI focused on implementing robust monitoring and observability solutions. Your tasks include:
1. Setting up logging and monitoring tools
2. Creating dashboards for key metrics
3. Implementing alerting systems
4. Ensuring comprehensive system observability
5. Providing guidance on interpreting monitoring data""",
    
    "diagram_creator": """You are a Diagram Creator AI specialized in creating various types of diagrams using Mermaid syntax. Your responsibilities include:
1. Creating system architecture diagrams
2. Designing user flow diagrams
3. Developing code structure and class diagrams
4. Illustrating infrastructure layouts
5. Ensuring diagrams are clear, informative, and follow best practices"""
}

AVAILABLE_AGENTS = [
    # ... existing agents ...
    "implementation_developer",
    "infrastructure_engineer",
    "monitoring_specialist",
    "diagram_creator"
]
```

## 3. Implement New Workflow Stages

Update the project processing to include new stages:

```python
# coordinator/project_operations.py

async def process_project(name: str, description: str, force: bool, process_rfcs: bool = True, implement_rfcs: bool = False):
    # ... existing code ...

    if implement_rfcs:
        print("\nImplementing accepted RFCs...")
        accepted_rfcs = [task for task in get_tasks(project_definition.name) if task.task_type == TaskType.RFC and task.rfc_state == RFCState.APPROVED]
        for rfc in accepted_rfcs:
            await implement_rfc(rfc, project_definition)

async def implement_rfc(rfc: Task, project_definition: ProjectDefinition):
    # Create implementation tasks
    implementation_task = await create_implementation_task(rfc, project_definition)
    infra_task = await create_infrastructure_task(rfc, project_definition)
    monitoring_task = await create_monitoring_task(rfc, project_definition)
    diagram_tasks = await create_diagram_tasks(rfc, project_definition)
    
    # Process each task
    await process_implementation_task(implementation_task)
    await process_infrastructure_task(infra_task)
    await process_monitoring_task(monitoring_task)
    for diagram_task in diagram_tasks:
        await process_diagram_task(diagram_task)

async def create_implementation_task(rfc: Task, project_definition: ProjectDefinition) -> Task:
    # Logic to create an implementation task based on the RFC
    pass

async def process_implementation_task(task: Task):
    # Logic to generate actual code based on the implementation task
    pass

# Similar functions for infrastructure, monitoring, and diagram tasks
```

## 4. Code Generation and Storage

Implement functions to generate and store actual code:

```python
# coordinator/code_generation.py

def generate_code(task: Task) -> str:
    # Use LLM to generate code based on the task
    pass

def save_code(project_name: str, filename: str, code: str):
    project_path = os.path.join("projects", project_name, "code")
    os.makedirs(project_path, exist_ok=True)
    with open(os.path.join(project_path, filename), "w") as f:
        f.write(code)
```

## 5. Diagram Generation

Implement functions to generate Mermaid diagrams:

```python
# coordinator/diagram_generation.py

def generate_mermaid_diagram(task: Task) -> str:
    # Use LLM to generate Mermaid syntax for the diagram
    pass

def save_diagram(project_name: str, diagram_name: str, mermaid_syntax: str):
    project_path = os.path.join("projects", project_name, "diagrams")
    os.makedirs(project_path, exist_ok=True)
    with open(os.path.join(project_path, f"{diagram_name}.mmd"), "w") as f:
        f.write(mermaid_syntax)
```

## 6. Update Main CLI

Update the main CLI to include new options:

```python
# coordinator/main.py

@click.command()
@click.option("--name", help="Project name")
@click.option("--description", help="Project description")
@click.option("--force", is_flag=True, help="Force task decomposition even if tasks already exist")
@click.option("--process-rfcs", is_flag=True, help="Process and update RFC tasks")
@click.option("--implement-rfcs", is_flag=True, help="Implement accepted RFCs")
def main(name: str, description: str, force: bool, process_rfcs: bool, implement_rfcs: bool):
    async def async_main():
        # ... existing code ...
        if name:
            if description or force:
                await process_project(name, description, force, process_rfcs, implement_rfcs)
            else:
                show_project_tasks(name)
    
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
```

## Next Steps

1. Implement the outlined functions, especially those in `project_operations.py`, `code_generation.py`, and `diagram_generation.py`.
2. Update the database schema and operations to accommodate new task types and states.
3. Implement proper error handling and logging throughout the new functions.
4. Create unit tests for the new functionality.
5. Update the documentation to reflect the new capabilities and usage.
6. Consider implementing a review system for generated code and diagrams.
7. Develop a system to track dependencies between implementation, infrastructure, and monitoring tasks.

This expanded system will now be capable of not only managing RFCs but also implementing them into actual code, setting up infrastructure, establishing monitoring, and creating various diagrams. The modular design allows for easy extension and modification of each stage in the future.

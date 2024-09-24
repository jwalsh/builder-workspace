# RFC Review, Approval, and Implementation Plan

## 1. Update Models

First, we need to update our `models.py` file to include new states and task types:

```python
# coordinator/models.py

class RFCState(str, Enum):
    # ... existing states ...
    PENDING_REVIEW = "PENDING_REVIEW"
    IN_REVIEW = "IN_REVIEW"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    IMPLEMENTING = "IMPLEMENTING"

class TaskType(str, Enum):
    # ... existing types ...
    RFC_REVIEW = "rfc_review"
    IMPLEMENTATION = "implementation"

class Task(BaseModel):
    # ... existing fields ...
    review_comments: Optional[str] = None
    approver: Optional[str] = None
```

## 2. Update RFC Processing

Modify `coordinator/project_operations/rfc_processing.py`:

```python
async def process_rfc(task: Task, project_definition: ProjectDefinition) -> List[Task]:
    # ... existing code ...

    if updated_task.rfc_state == RFCState.DRAFT:
        updated_task.rfc_state = RFCState.PENDING_REVIEW
        review_task = create_review_task(updated_task, project_definition)
        return [updated_task, review_task]
    
    return [updated_task]

def create_review_task(rfc_task: Task, project_definition: ProjectDefinition) -> Task:
    return Task(
        id=0,
        project_id=project_definition.name,
        title=f"Review RFC: {rfc_task.title}",
        description=f"Review the RFC '{rfc_task.title}' (Task ID: {rfc_task.id})",
        status="TODO",
        assigned_to="project-manager",
        priority=rfc_task.priority,
        dependencies=[str(rfc_task.id)],
        task_type=TaskType.RFC_REVIEW
    )
```

## 3. Implement RFC Review Process

Create a new file `coordinator/project_operations/rfc_review.py`:

```python
from ..models import Task, RFCState, TaskType
from ..db import update_task
from ..llm import llm_manager

async def review_rfc(review_task: Task, rfc_task: Task) -> List[Task]:
    prompt = f"""Review the following RFC:

Title: {rfc_task.title}
Description: {rfc_task.description}

Please provide a review with the following structure:
{{
  "approved": true/false,
  "comments": "Detailed review comments",
  "next_steps": "Suggested next steps or changes"
}}"""

    review_response = await llm_manager.run_llm_command(prompt, f"review_rfc_{rfc_task.id}", "project-manager")
    review_data = extract_json_from_response(review_response)

    rfc_task.rfc_state = RFCState.APPROVED if review_data["approved"] else RFCState.REJECTED
    rfc_task.review_comments = review_data["comments"]
    update_task(rfc_task)

    review_task.status = "COMPLETED"
    update_task(review_task)

    if rfc_task.rfc_state == RFCState.APPROVED:
        implementation_task = create_implementation_task(rfc_task)
        return [rfc_task, review_task, implementation_task]
    
    return [rfc_task, review_task]

def create_implementation_task(rfc_task: Task) -> Task:
    return Task(
        id=0,
        project_id=rfc_task.project_id,
        title=f"Implement: {rfc_task.title}",
        description=f"Implement the approved RFC '{rfc_task.title}' (Task ID: {rfc_task.id})",
        status="TODO",
        assigned_to="code-architect",
        priority=rfc_task.priority,
        dependencies=[str(rfc_task.id)],
        task_type=TaskType.IMPLEMENTATION
    )
```

## 4. Update Project Management

Modify `coordinator/project_operations/project_management.py`:

```python
from .rfc_review import review_rfc

async def process_project(name: str, description: str, force: bool, process_rfcs: bool = True):
    # ... existing code ...

    if process_rfcs:
        print("\nProcessing RFC tasks...")
        rfc_tasks = [task for task in get_tasks(project_definition.name) if task.task_type == TaskType.RFC]
        review_tasks = [task for task in get_tasks(project_definition.name) if task.task_type == TaskType.RFC_REVIEW]
        
        for rfc_task in rfc_tasks:
            try:
                updated_tasks = await process_rfc(rfc_task, project_definition)
                for task in updated_tasks:
                    if task.id == 0:
                        add_task(task)
                    else:
                        update_task(task)
                print(f"Processed RFC task: {rfc_task.title} (New state: {rfc_task.rfc_state})")
            except Exception as e:
                logging.error(f"Error processing RFC task {rfc_task.id}: {str(e)}")

        for review_task in review_tasks:
            if review_task.status == "TODO":
                rfc_task = next(task for task in rfc_tasks if str(task.id) in review_task.dependencies)
                try:
                    updated_tasks = await review_rfc(review_task, rfc_task)
                    for task in updated_tasks:
                        update_task(task)
                    print(f"Reviewed RFC: {rfc_task.title} (New state: {rfc_task.rfc_state})")
                except Exception as e:
                    logging.error(f"Error reviewing RFC task {rfc_task.id}: {str(e)}")

    # ... rest of the function ...
```

## 5. Update CLI

Modify `coordinator/main.py` to include options for reviewing RFCs and starting implementation:

```python
@click.option("--review-rfcs", is_flag=True, help="Review pending RFCs")
@click.option("--start-implementation", is_flag=True, help="Start implementation of approved RFCs")
def main(name: str, description: str, force: bool, process_rfcs: bool, review_rfcs: bool, start_implementation: bool):
    # ... existing code ...
    
    if review_rfcs:
        # Add logic to review RFCs
        pass
    
    if start_implementation:
        # Add logic to start implementation of approved RFCs
        pass

    # ... rest of the function ...
```

## Next Steps

1. Implement the scaffolded functions and integrate them into your existing codebase.
2. Add unit tests for the new functionality.
3. Update your documentation to reflect the new RFC review and approval process.
4. Consider adding a user interface or CLI commands for manual review and approval of RFCs.
5. Implement the actual logic for starting the implementation of approved RFCs.


# RFC to Implementation Task Workflow

## 1. RFC Approval

- When an RFC's state changes to APPROVED, trigger the transition process.

## 2. Task Creation

1. Create a new "Implementation Planning" task:
   - Title: "Plan Implementation for RFC-[RFC_NUMBER]: [RFC_TITLE]"
   - Assigned to: Project Manager or Technical Lead
   - Description: Include link to the approved RFC and request breakdown into subtasks

2. The assigned person creates subtasks based on the RFC:
   - Each subtask should represent a concrete, actionable item
   - Subtasks should cover all aspects: development, testing, documentation, etc.
   - Use the Task model with appropriate fields (title, description, assigned_to, priority, etc.)

## 3. Task Assignment

- Assign each subtask to the appropriate team member or role (e.g., frontend-developer, backend-developer, etc.)
- Set initial status as "TODO" for all subtasks

## 4. Implementation Kickoff

- Schedule a kickoff meeting with all assigned team members
- Review the RFC and all created subtasks
- Address any questions or concerns

## 5. Progress Tracking

- Update task statuses as work progresses (e.g., TODO -> IN_PROGRESS -> REVIEW -> DONE)
- Regular check-ins (e.g., daily stand-ups) to discuss progress and blockers

## 6. Quality Assurance

- Include specific tasks for testing and code review
- Ensure all acceptance criteria from the RFC are covered in the tasks

## 7. Documentation

- Include tasks for updating relevant documentation
- Ensure user guides, API docs, etc. are updated as part of the implementation

## 8. Final Review

- Once all subtasks are completed, conduct a final review
- Verify that all aspects of the RFC have been implemented correctly

## 9. Closure

- Mark the main "Implementation Planning" task as complete
- Update the RFC status to IMPLEMENTED

## 10. Retrospective

- Conduct a brief retrospective to gather learnings from the implementation process
- Use insights to improve future RFC implementations

# File: coordinator/implementation_workflow.py

from typing import List

from .db import add_task, get_tasks, update_task
from .models import ImplementationPlan, RFCState, Task, TaskType


def create_implementation_plan(rfc_task: Task) -> ImplementationPlan:
    planning_task = Task(
        id=0,
        project_id=rfc_task.project_id,
        title=f"Plan Implementation for RFC-{rfc_task.id}: {rfc_task.title}",
        description=f"Create implementation plan for approved RFC: {rfc_task.title}",
        status="TODO",
        assigned_to="project-manager",
        priority=rfc_task.priority,
        task_type=TaskType.IMPLEMENTATION_PLANNING,
        dependencies=[str(rfc_task.id)],  # Use dependencies to link to the RFC task
    )
    planning_task_id = add_task(planning_task)

    return ImplementationPlan(
        rfc_id=rfc_task.id, planning_task_id=planning_task_id, subtasks=[]
    )


def add_implementation_subtask(plan: ImplementationPlan, subtask: Task) -> int:
    subtask.dependencies = [str(plan.planning_task_id)]  # Link to the planning task
    subtask_id = add_task(subtask)
    plan.subtasks.append(subtask_id)
    return subtask_id


def complete_implementation(plan: ImplementationPlan):
    # Get all tasks for the project
    all_tasks = get_tasks(plan.rfc_id)  # Assuming rfc_id is the project_id

    # Find the RFC task and update its state
    rfc_task = next((task for task in all_tasks if task.id == plan.rfc_id), None)
    if rfc_task:
        rfc_task.rfc_state = RFCState.IMPLEMENTED
        update_task(rfc_task)

    # Find the planning task and update its status
    planning_task = next(
        (task for task in all_tasks if task.id == plan.planning_task_id), None
    )
    if planning_task:
        planning_task.status = "COMPLETED"
        update_task(planning_task)


# Add more functions as needed for the workflow

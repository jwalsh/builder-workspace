# File: coordinator/parallel_decomposition.py

import asyncio
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from threading import Lock
from typing import List, Dict

from .models import ProjectDefinition, Task
from .project_operations.decompose import decompose_project
from .llm import llm_manager


class DecompositionLeader:
    def __init__(self, project_definition: ProjectDefinition, num_runners: int = 4):
        self.project_definition = project_definition
        self.num_runners = num_runners
        self.work_queue = Queue()
        self.results = []
        self.lock = Lock()

    async def generate_work_queue(self):
        # Generate high-level tasks
        high_level_tasks = await decompose_project(self.project_definition)

        # Add high-level tasks to the work queue
        for task in high_level_tasks:
            self.work_queue.put(task)

    async def process_results(self):
        while (
            not self.work_queue.empty() or len(self.results) < self.work_queue.qsize()
        ):
            await asyncio.sleep(0.1)  # Avoid busy waiting

        # Process and consolidate results
        all_tasks = []
        for result in self.results:
            all_tasks.extend(result)

        return all_tasks


class DecompositionRunner:
    def __init__(self, work_queue: Queue, results: List, lock: Lock):
        self.work_queue = work_queue
        self.results = results
        self.lock = lock

    async def run(self):
        while not self.work_queue.empty():
            task = self.work_queue.get()
            subtasks = await self.decompose_task(task)

            with self.lock:
                self.results.append(subtasks)

            self.work_queue.task_done()

    async def decompose_task(self, task: Task) -> List[Task]:
        # Use LLM to decompose the task into subtasks
        prompt = f"Decompose the following task into smaller subtasks:\n\n{task.title}\n{task.description}"
        response = await llm_manager.run_llm_command(
            prompt, f"decompose_{task.id}", "task-decomposer"
        )

        # Parse the response and create subtasks
        # (You'll need to implement the parsing logic based on your LLM's output format)
        subtasks = parse_subtasks_from_response(response, task.project_id)

        return subtasks


def parse_subtasks_from_response(response: str, project_id: str) -> List[Task]:
    # Implement parsing logic here
    # This should convert the LLM's response into a list of Task objects
    pass


async def parallel_decompose_project(
    project_definition: ProjectDefinition, num_runners: int = 4
) -> List[Task]:
    leader = DecompositionLeader(project_definition, num_runners)
    await leader.generate_work_queue()

    runners = [
        DecompositionRunner(leader.work_queue, leader.results, leader.lock)
        for _ in range(num_runners)
    ]

    with ThreadPoolExecutor(max_workers=num_runners) as executor:
        loop = asyncio.get_event_loop()
        runner_tasks = [
            loop.run_in_executor(executor, runner.run) for runner in runners
        ]
        await asyncio.gather(*runner_tasks)

    return await leader.process_results()


# Update the main process_project function to use parallel decomposition
async def process_project(
    name: str, description: str, force: bool, num_runners: int = 4
):
    project_definition = ProjectDefinition(name=name, description=description)

    if force or not get_tasks(project_definition.name):
        print(
            f"\nDecomposing project '{project_definition.name}' into tasks using {num_runners} parallel runners..."
        )
        tasks = await parallel_decompose_project(project_definition, num_runners)

        for task in tasks:
            task_id = add_task(task)
            if task_id:
                print(
                    f"Added task: {task.title} (Type: {task.task_type}, Assigned to: {task.assigned_to})"
                )
            else:
                logging.error(f"Failed to add task: {task.title}")

        create_project_directory(
            project_definition.name, project_definition.description, tasks
        )
    else:
        print(
            f"\nTasks already exist for project '{project_definition.name}'. Use --force to override."
        )

    # Continue with the rest of the process_project function...

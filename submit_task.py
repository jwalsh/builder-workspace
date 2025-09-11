#!/usr/bin/env python3
# submit_task.py - Submit tasks to the queue for Claude agents

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional

# Add coordinator to path
sys.path.insert(0, str(Path(__file__).parent))

from coordinator.advanced_queue import QueueTask, Priority, TaskQueue


async def submit_implementation_task(description: str, file_path: str, priority: Priority = Priority.NORMAL):
    """Submit an implementation task to the queue"""
    queue = TaskQueue()
    await queue.connect()
    
    task = QueueTask(
        task_type="implementation",
        payload={
            "description": description,
            "file_path": file_path,
            "instructions": f"Implement the following: {description}"
        },
        priority=priority
    )
    
    task_id = await queue.enqueue(task)
    print(f"Submitted implementation task: {task_id}")
    
    await queue.disconnect()
    return task_id


async def submit_testing_task(description: str, file_path: str, depends_on: Optional[str] = None):
    """Submit a testing task to the queue"""
    queue = TaskQueue()
    await queue.connect()
    
    task = QueueTask(
        task_type="testing",
        payload={
            "description": description,
            "file_path": file_path,
            "instructions": f"Write tests for: {description}"
        },
        priority=Priority.NORMAL,
        dependencies={depends_on} if depends_on else set()
    )
    
    task_id = await queue.enqueue(task)
    print(f"Submitted testing task: {task_id}")
    
    await queue.disconnect()
    return task_id


async def submit_batch_tasks():
    """Submit a batch of example tasks"""
    queue = TaskQueue()
    await queue.connect()
    
    tasks = [
        # High priority implementation tasks
        QueueTask(
            task_type="implementation",
            payload={
                "description": "Create user authentication module",
                "file_path": "coordinator/auth/user_auth.py",
                "requirements": [
                    "JWT token generation",
                    "Password hashing with bcrypt",
                    "Session management",
                    "Rate limiting"
                ]
            },
            priority=Priority.HIGH
        ),
        
        QueueTask(
            task_type="implementation",
            payload={
                "description": "Build task scheduler service",
                "file_path": "coordinator/scheduler/task_scheduler.py",
                "requirements": [
                    "Cron-like scheduling",
                    "Task retry logic",
                    "Priority queue management",
                    "Worker pool coordination"
                ]
            },
            priority=Priority.HIGH
        ),
        
        # Normal priority tasks
        QueueTask(
            task_type="implementation",
            payload={
                "description": "Create logging middleware",
                "file_path": "coordinator/middleware/logging.py",
                "requirements": [
                    "Structured logging",
                    "Log rotation",
                    "Performance metrics",
                    "Error tracking"
                ]
            },
            priority=Priority.NORMAL
        ),
        
        # Testing tasks
        QueueTask(
            task_type="testing",
            payload={
                "description": "Test authentication module",
                "file_path": "tests/test_user_auth.py",
                "test_requirements": [
                    "Unit tests for JWT generation",
                    "Integration tests for login flow",
                    "Security tests for rate limiting",
                    "Edge case handling"
                ]
            },
            priority=Priority.NORMAL
        ),
        
        QueueTask(
            task_type="testing", 
            payload={
                "description": "Test task scheduler",
                "file_path": "tests/test_scheduler.py",
                "test_requirements": [
                    "Scheduling accuracy tests",
                    "Concurrency tests",
                    "Failure recovery tests",
                    "Performance benchmarks"
                ]
            },
            priority=Priority.NORMAL
        )
    ]
    
    submitted_ids = []
    for task in tasks:
        task_id = await queue.enqueue(task)
        submitted_ids.append(task_id)
        print(f"Submitted {task.task_type} task: {task_id[:8]} - {task.payload['description']}")
    
    await queue.disconnect()
    
    print(f"\n✅ Submitted {len(submitted_ids)} tasks to the queue")
    print("\nTasks will be processed by the Claude agents in the tmux sessions.")
    print("Monitor progress with: tmux attach -t queue-monitor")
    
    return submitted_ids


async def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "batch":
            await submit_batch_tasks()
        elif command == "impl":
            if len(sys.argv) < 4:
                print("Usage: submit_task.py impl <description> <file_path>")
                sys.exit(1)
            await submit_implementation_task(sys.argv[2], sys.argv[3])
        elif command == "test":
            if len(sys.argv) < 4:
                print("Usage: submit_task.py test <description> <file_path>")
                sys.exit(1)
            await submit_testing_task(sys.argv[2], sys.argv[3])
        else:
            print(f"Unknown command: {command}")
            print("Available commands: batch, impl, test")
    else:
        print("Queue Task Submission Tool")
        print("=" * 40)
        print("\nUsage:")
        print("  ./submit_task.py batch                    # Submit example batch of tasks")
        print("  ./submit_task.py impl <desc> <file>       # Submit implementation task")
        print("  ./submit_task.py test <desc> <file>       # Submit testing task")
        print("\nExample:")
        print("  ./submit_task.py impl 'Create API endpoint' 'api/endpoint.py'")
        print("  ./submit_task.py test 'Test API endpoint' 'tests/test_endpoint.py'")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCancelled")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
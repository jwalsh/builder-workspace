# File: coordinator/advanced_queue.py

import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
from uuid import uuid4

import aioredis
from pydantic import BaseModel


class Priority(Enum):
    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4
    DEFERRED = 5


class TaskStatus(Enum):
    QUEUED = "queued"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"
    CANCELLED = "cancelled"


@dataclass
class QueueTask:
    id: str = field(default_factory=lambda: str(uuid4()))
    task_type: str = ""
    payload: Dict[str, Any] = field(default_factory=dict)
    priority: Priority = Priority.NORMAL
    status: TaskStatus = TaskStatus.QUEUED
    created_at: datetime = field(default_factory=datetime.now)
    assigned_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    agent_id: Optional[str] = None
    retry_count: int = 0
    max_retries: int = 3
    dependencies: Set[str] = field(default_factory=set)
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class TaskQueue:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_url = redis_url
        self.redis: Optional[aioredis.Redis] = None
        self.logger = logging.getLogger(__name__)
        
    async def connect(self):
        """Connect to Redis backend"""
        self.redis = await aioredis.from_url(self.redis_url)
        
    async def disconnect(self):
        """Disconnect from Redis"""
        if self.redis:
            await self.redis.close()
            
    async def enqueue(self, task: QueueTask) -> str:
        """Add task to queue"""
        task_json = json.dumps({
            "id": task.id,
            "task_type": task.task_type,
            "payload": task.payload,
            "priority": task.priority.value,
            "status": task.status.value,
            "created_at": task.created_at.isoformat(),
            "retry_count": task.retry_count,
            "max_retries": task.max_retries,
            "dependencies": list(task.dependencies)
        })
        
        # Add to priority queue
        await self.redis.zadd(
            f"queue:{task.task_type}", 
            {task_json: task.priority.value}
        )
        
        # Store task details
        await self.redis.hset(
            f"task:{task.id}",
            mapping={
                "data": task_json,
                "status": task.status.value
            }
        )
        
        self.logger.info(f"Enqueued task {task.id} with priority {task.priority}")
        return task.id
        
    async def dequeue(self, task_type: str, agent_id: str) -> Optional[QueueTask]:
        """Get next task from queue for agent"""
        # Get highest priority task
        result = await self.redis.zpopmin(f"queue:{task_type}")
        
        if not result:
            return None
            
        task_json, _ = result[0]
        task_data = json.loads(task_json)
        
        # Check dependencies
        if task_data.get("dependencies"):
            for dep_id in task_data["dependencies"]:
                dep_status = await self.redis.hget(f"task:{dep_id}", "status")
                if dep_status != TaskStatus.COMPLETED.value:
                    # Re-queue task if dependencies not met
                    await self.redis.zadd(
                        f"queue:{task_type}",
                        {task_json: task_data["priority"]}
                    )
                    return None
        
        # Create task object
        task = QueueTask(
            id=task_data["id"],
            task_type=task_data["task_type"],
            payload=task_data["payload"],
            priority=Priority(task_data["priority"]),
            status=TaskStatus.ASSIGNED,
            created_at=datetime.fromisoformat(task_data["created_at"]),
            assigned_at=datetime.now(),
            agent_id=agent_id,
            retry_count=task_data["retry_count"],
            max_retries=task_data["max_retries"],
            dependencies=set(task_data.get("dependencies", []))
        )
        
        # Update task status
        await self.redis.hset(
            f"task:{task.id}",
            mapping={
                "status": TaskStatus.ASSIGNED.value,
                "agent_id": agent_id,
                "assigned_at": task.assigned_at.isoformat()
            }
        )
        
        self.logger.info(f"Assigned task {task.id} to agent {agent_id}")
        return task
        
    async def complete_task(self, task_id: str, result: Dict[str, Any]):
        """Mark task as completed"""
        await self.redis.hset(
            f"task:{task_id}",
            mapping={
                "status": TaskStatus.COMPLETED.value,
                "completed_at": datetime.now().isoformat(),
                "result": json.dumps(result)
            }
        )
        self.logger.info(f"Completed task {task_id}")
        
    async def fail_task(self, task_id: str, error: str):
        """Mark task as failed and potentially retry"""
        task_data = await self.redis.hget(f"task:{task_id}", "data")
        if not task_data:
            return
            
        task_info = json.loads(task_data)
        retry_count = task_info.get("retry_count", 0)
        max_retries = task_info.get("max_retries", 3)
        
        if retry_count < max_retries:
            # Retry task
            task_info["retry_count"] = retry_count + 1
            task_info["status"] = TaskStatus.RETRYING.value
            
            await self.redis.zadd(
                f"queue:{task_info['task_type']}",
                {json.dumps(task_info): Priority.HIGH.value}
            )
            
            await self.redis.hset(
                f"task:{task_id}",
                mapping={
                    "status": TaskStatus.RETRYING.value,
                    "retry_count": str(retry_count + 1),
                    "last_error": error
                }
            )
            self.logger.info(f"Retrying task {task_id} (attempt {retry_count + 1})")
        else:
            # Mark as permanently failed
            await self.redis.hset(
                f"task:{task_id}",
                mapping={
                    "status": TaskStatus.FAILED.value,
                    "failed_at": datetime.now().isoformat(),
                    "error": error
                }
            )
            self.logger.error(f"Task {task_id} permanently failed: {error}")
            
    async def get_queue_stats(self) -> Dict[str, Any]:
        """Get queue statistics"""
        stats = {
            "queues": {},
            "total_tasks": 0,
            "by_status": {}
        }
        
        # Get all queue keys
        queues = await self.redis.keys("queue:*")
        for queue_key in queues:
            queue_name = queue_key.decode().split(":", 1)[1]
            queue_size = await self.redis.zcard(queue_key)
            stats["queues"][queue_name] = queue_size
            stats["total_tasks"] += queue_size
            
        # Get task status counts
        tasks = await self.redis.keys("task:*")
        for task_key in tasks:
            status = await self.redis.hget(task_key, "status")
            if status:
                status = status.decode()
                stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
                
        return stats


class AgentWorker:
    def __init__(self, agent_id: str, task_types: List[str], queue: TaskQueue):
        self.agent_id = agent_id
        self.task_types = task_types
        self.queue = queue
        self.running = False
        self.logger = logging.getLogger(f"Agent-{agent_id}")
        
    async def start(self):
        """Start processing tasks"""
        self.running = True
        self.logger.info(f"Agent {self.agent_id} started")
        
        while self.running:
            for task_type in self.task_types:
                task = await self.queue.dequeue(task_type, self.agent_id)
                
                if task:
                    try:
                        self.logger.info(f"Processing task {task.id}")
                        result = await self.process_task(task)
                        await self.queue.complete_task(task.id, result)
                    except Exception as e:
                        self.logger.error(f"Task {task.id} failed: {e}")
                        await self.queue.fail_task(task.id, str(e))
                        
            await asyncio.sleep(1)  # Polling interval
            
    async def stop(self):
        """Stop processing"""
        self.running = False
        self.logger.info(f"Agent {self.agent_id} stopped")
        
    async def process_task(self, task: QueueTask) -> Dict[str, Any]:
        """Process a single task - override in subclasses"""
        # Simulate work
        await asyncio.sleep(2)
        return {"status": "success", "agent": self.agent_id}


class QueueOrchestrator:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.queue = TaskQueue(redis_url)
        self.agents: Dict[str, AgentWorker] = {}
        self.logger = logging.getLogger("Orchestrator")
        
    async def start(self):
        """Start the orchestrator"""
        await self.queue.connect()
        self.logger.info("Queue orchestrator started")
        
    async def stop(self):
        """Stop the orchestrator"""
        # Stop all agents
        for agent in self.agents.values():
            await agent.stop()
            
        await self.queue.disconnect()
        self.logger.info("Queue orchestrator stopped")
        
    async def add_agent(self, agent_id: str, task_types: List[str]) -> AgentWorker:
        """Add a new agent worker"""
        agent = AgentWorker(agent_id, task_types, self.queue)
        self.agents[agent_id] = agent
        asyncio.create_task(agent.start())
        self.logger.info(f"Added agent {agent_id} for tasks: {task_types}")
        return agent
        
    async def submit_task(self, task: QueueTask) -> str:
        """Submit a task to the queue"""
        return await self.queue.enqueue(task)
        
    async def get_status(self) -> Dict[str, Any]:
        """Get orchestrator status"""
        stats = await self.queue.get_queue_stats()
        stats["agents"] = {
            agent_id: {
                "task_types": agent.task_types,
                "running": agent.running
            }
            for agent_id, agent in self.agents.items()
        }
        return stats


# Example usage
async def main():
    # Initialize orchestrator
    orchestrator = QueueOrchestrator()
    await orchestrator.start()
    
    # Add agents
    await orchestrator.add_agent("agent-1", ["implementation", "testing"])
    await orchestrator.add_agent("agent-2", ["documentation", "review"])
    
    # Submit tasks
    tasks = [
        QueueTask(
            task_type="implementation",
            payload={"file": "feature.py", "description": "Implement new feature"},
            priority=Priority.HIGH
        ),
        QueueTask(
            task_type="documentation",
            payload={"file": "README.md", "description": "Update documentation"},
            priority=Priority.NORMAL
        ),
        QueueTask(
            task_type="testing",
            payload={"file": "test_feature.py", "description": "Write tests"},
            priority=Priority.HIGH,
            dependencies={"task-1"}  # Depends on implementation
        )
    ]
    
    for task in tasks:
        task_id = await orchestrator.submit_task(task)
        print(f"Submitted task: {task_id}")
    
    # Monitor status
    while True:
        status = await orchestrator.get_status()
        print(f"Queue status: {json.dumps(status, indent=2)}")
        await asyncio.sleep(5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
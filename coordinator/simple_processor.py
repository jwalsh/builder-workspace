#!/usr/bin/env python3
"""
Simple task processor for demonstration
Created: 2025-01-10
Purpose: Demonstrate basic task processing with the queue system
"""

import asyncio
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from redis_wrapper import RedisWrapper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SimpleTaskProcessor:
    """
    Minimal task processor that demonstrates the queue system.
    Processes simple text transformation and file generation tasks.
    """
    
    def __init__(self, processor_id: str = "simple-processor-1"):
        self.processor_id = processor_id
        self.redis = RedisWrapper(use_redis=False)  # Start with in-memory for testing
        self.processed_count = 0
        self.start_time = datetime.now()
        
    async def connect(self):
        """Initialize connection"""
        connected = await self.redis.connect()
        logger.info(f"Processor {self.processor_id} initialized (storage: {self.redis.get_stats()['type']})")
        return connected
        
    async def process_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a single task based on its type.
        
        Supported task types:
        - text_transform: Apply text transformations
        - file_generate: Generate simple files
        - data_analyze: Perform basic data analysis
        """
        task_type = task_data.get('type', 'unknown')
        payload = task_data.get('payload', {})
        
        logger.info(f"Processing {task_type} task: {task_data.get('id', 'unknown')}")
        
        try:
            if task_type == 'text_transform':
                result = await self._process_text_transform(payload)
            elif task_type == 'file_generate':
                result = await self._process_file_generate(payload)
            elif task_type == 'data_analyze':
                result = await self._process_data_analyze(payload)
            else:
                result = {"error": f"Unknown task type: {task_type}"}
                
            self.processed_count += 1
            return {
                "success": True,
                "processor": self.processor_id,
                "task_id": task_data.get('id'),
                "result": result,
                "processed_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Task processing failed: {e}")
            return {
                "success": False,
                "processor": self.processor_id,
                "task_id": task_data.get('id'),
                "error": str(e),
                "failed_at": datetime.now().isoformat()
            }
            
    async def _process_text_transform(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process text transformation tasks"""
        text = payload.get('text', '')
        operations = payload.get('operations', [])
        
        result = text
        for op in operations:
            if op == 'uppercase':
                result = result.upper()
            elif op == 'lowercase':
                result = result.lower()
            elif op == 'reverse':
                result = result[::-1]
            elif op == 'remove_spaces':
                result = result.replace(' ', '')
                
        return {
            "original": text,
            "transformed": result,
            "operations_applied": operations
        }
        
    async def _process_file_generate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process file generation tasks"""
        filename = payload.get('filename', f'generated_{datetime.now().timestamp()}.txt')
        content = payload.get('content', '')
        output_dir = Path('output/generated')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = output_dir / filename
        filepath.write_text(content)
        
        return {
            "filename": filename,
            "path": str(filepath),
            "size": len(content),
            "created": True
        }
        
    async def _process_data_analyze(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process data analysis tasks"""
        data = payload.get('data', [])
        analysis_type = payload.get('analysis', 'basic')
        
        if not data:
            return {"error": "No data provided"}
            
        if analysis_type == 'basic':
            return {
                "count": len(data),
                "unique": len(set(data)),
                "first": data[0] if data else None,
                "last": data[-1] if data else None
            }
        elif analysis_type == 'numeric':
            numeric_data = [x for x in data if isinstance(x, (int, float))]
            if numeric_data:
                return {
                    "count": len(numeric_data),
                    "sum": sum(numeric_data),
                    "min": min(numeric_data),
                    "max": max(numeric_data),
                    "avg": sum(numeric_data) / len(numeric_data)
                }
            return {"error": "No numeric data found"}
            
        return {"error": f"Unknown analysis type: {analysis_type}"}
        
    def get_stats(self) -> Dict[str, Any]:
        """Get processor statistics"""
        uptime = (datetime.now() - self.start_time).total_seconds()
        return {
            "processor_id": self.processor_id,
            "processed_count": self.processed_count,
            "uptime_seconds": uptime,
            "rate_per_minute": (self.processed_count / uptime * 60) if uptime > 0 else 0,
            "storage": self.redis.get_stats()
        }


async def demo_processing():
    """Demonstrate the simple processor with sample tasks"""
    
    # Initialize processor
    processor = SimpleTaskProcessor("demo-processor")
    await processor.connect()
    
    # Sample tasks
    tasks = [
        {
            "id": "task-001",
            "type": "text_transform",
            "payload": {
                "text": "Hello World from Queue System",
                "operations": ["uppercase", "reverse"]
            }
        },
        {
            "id": "task-002",
            "type": "file_generate",
            "payload": {
                "filename": "queue_test.txt",
                "content": "This file was generated by the queue system\nTimestamp: " + datetime.now().isoformat()
            }
        },
        {
            "id": "task-003",
            "type": "data_analyze",
            "payload": {
                "data": [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
                "analysis": "numeric"
            }
        },
        {
            "id": "task-004",
            "type": "data_analyze",
            "payload": {
                "data": ["apple", "banana", "apple", "cherry", "banana", "date"],
                "analysis": "basic"
            }
        }
    ]
    
    # Process tasks
    results = []
    for task in tasks:
        logger.info(f"\n--- Processing Task {task['id']} ---")
        result = await processor.process_task(task)
        results.append(result)
        logger.info(f"Result: {json.dumps(result, indent=2)}")
        await asyncio.sleep(0.5)  # Simulate processing time
        
    # Display statistics
    stats = processor.get_stats()
    logger.info(f"\n--- Processor Statistics ---")
    logger.info(f"Total processed: {stats['processed_count']}")
    logger.info(f"Processing rate: {stats['rate_per_minute']:.2f} tasks/minute")
    logger.info(f"Storage type: {stats['storage']['type']}")
    
    # Save results
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    results_file = output_dir / f"processing_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    results_file.write_text(json.dumps({
        "processor": processor.processor_id,
        "timestamp": datetime.now().isoformat(),
        "tasks_processed": len(results),
        "results": results,
        "statistics": stats
    }, indent=2))
    
    logger.info(f"\nResults saved to: {results_file}")
    
    return results


if __name__ == "__main__":
    # Run demonstration
    asyncio.run(demo_processing())
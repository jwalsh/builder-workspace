#!/usr/bin/env python3
# coordinator/queue_status.py - Monitor queue status

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    import aioredis
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.text import Text
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "aioredis", "rich"])
    import aioredis
    from rich.console import Console
    from rich.table import Table
    from rich.live import Live
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.text import Text


class QueueMonitor:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_url = redis_url
        self.redis = None
        self.console = Console()
        
    async def connect(self):
        """Connect to Redis"""
        try:
            self.redis = await aioredis.from_url(self.redis_url)
            await self.redis.ping()
            return True
        except Exception as e:
            self.console.print(f"[red]Failed to connect to Redis: {e}[/red]")
            return False
            
    async def get_queue_stats(self):
        """Get current queue statistics"""
        stats = {
            "queues": {},
            "tasks_by_status": {},
            "agents": {},
            "recent_tasks": []
        }
        
        # Get queue sizes
        queue_keys = await self.redis.keys("queue:*")
        for key in queue_keys:
            queue_name = key.decode().split(":", 1)[1]
            size = await self.redis.zcard(key)
            stats["queues"][queue_name] = size
            
        # Get task counts by status
        task_keys = await self.redis.keys("task:*")
        for key in task_keys:
            status = await self.redis.hget(key, "status")
            if status:
                status = status.decode()
                stats["tasks_by_status"][status] = stats["tasks_by_status"].get(status, 0) + 1
                
            # Get recent task info
            task_data = await self.redis.hget(key, "data")
            if task_data:
                task_info = json.loads(task_data)
                created_at = datetime.fromisoformat(task_info.get("created_at", ""))
                if (datetime.now() - created_at).seconds < 300:  # Last 5 minutes
                    stats["recent_tasks"].append({
                        "id": task_info.get("id", "")[:8],
                        "type": task_info.get("task_type", ""),
                        "status": status.decode() if status else "unknown",
                        "created": created_at.strftime("%H:%M:%S")
                    })
                    
        # Sort recent tasks by creation time
        stats["recent_tasks"].sort(key=lambda x: x["created"], reverse=True)
        stats["recent_tasks"] = stats["recent_tasks"][:10]  # Keep only 10 most recent
        
        return stats
        
    def create_display(self, stats):
        """Create rich display layout"""
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body"),
            Layout(name="footer", size=3)
        )
        
        # Header
        header_text = Text("Queue Monitor Dashboard", style="bold blue")
        header_text.append(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style="dim")
        layout["header"].update(Panel(header_text, border_style="blue"))
        
        # Body - split into columns
        layout["body"].split_row(
            Layout(name="queues", ratio=1),
            Layout(name="tasks", ratio=1),
            Layout(name="recent", ratio=1)
        )
        
        # Queue status table
        queue_table = Table(title="Queue Status", border_style="green")
        queue_table.add_column("Queue", style="cyan")
        queue_table.add_column("Pending", justify="right", style="yellow")
        
        for queue_name, count in stats["queues"].items():
            queue_table.add_row(queue_name, str(count))
            
        if not stats["queues"]:
            queue_table.add_row("No queues", "-")
            
        layout["body"]["queues"].update(Panel(queue_table, border_style="green"))
        
        # Task status table
        task_table = Table(title="Task Status", border_style="yellow")
        task_table.add_column("Status", style="cyan")
        task_table.add_column("Count", justify="right")
        
        status_colors = {
            "queued": "white",
            "assigned": "yellow",
            "in_progress": "blue",
            "completed": "green",
            "failed": "red",
            "retrying": "magenta"
        }
        
        for status, count in stats["tasks_by_status"].items():
            color = status_colors.get(status, "white")
            task_table.add_row(
                Text(status.upper(), style=color),
                str(count)
            )
            
        if not stats["tasks_by_status"]:
            task_table.add_row("No tasks", "-")
            
        layout["body"]["tasks"].update(Panel(task_table, border_style="yellow"))
        
        # Recent tasks table
        recent_table = Table(title="Recent Tasks", border_style="magenta")
        recent_table.add_column("ID", style="dim")
        recent_table.add_column("Type", style="cyan")
        recent_table.add_column("Status", style="white")
        recent_table.add_column("Time", style="dim")
        
        for task in stats["recent_tasks"]:
            status_color = status_colors.get(task["status"].lower(), "white")
            recent_table.add_row(
                task["id"],
                task["type"],
                Text(task["status"], style=status_color),
                task["created"]
            )
            
        if not stats["recent_tasks"]:
            recent_table.add_row("-", "No recent tasks", "-", "-")
            
        layout["body"]["recent"].update(Panel(recent_table, border_style="magenta"))
        
        # Footer
        footer_text = Text("Press Ctrl+C to exit", style="dim")
        layout["footer"].update(Panel(footer_text, border_style="dim"))
        
        return layout
        
    async def monitor(self):
        """Main monitoring loop"""
        if not await self.connect():
            return
            
        with Live(self.create_display({}), refresh_per_second=0.5, console=self.console) as live:
            try:
                while True:
                    stats = await self.get_queue_stats()
                    live.update(self.create_display(stats))
                    await asyncio.sleep(2)
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Monitoring stopped[/yellow]")
            finally:
                if self.redis:
                    await self.redis.close()


async def main():
    monitor = QueueMonitor()
    await monitor.monitor()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
#!/usr/bin/env python3

import json
import sys
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProjectCoordinator:
    def __init__(self):
        self.tasks_file = "tasks.json"
        self.tasks = self.load_tasks()
        
    def load_tasks(self):
        try:
            with open(self.tasks_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading tasks: {e}")
            return None
            
    def get_active_tasks(self):
        return [task for task in self.tasks['coordinator_tasks'] 
                if task['status'] in ['active', 'ongoing']]
                
    def get_project_status(self):
        return {
            "BuilderAgents": 0.80,
            "MultilinguaStoryForge": 0.65,
            "SmartEnergyGrid": 0.45,
            "AISecurityAuditor": 0.35,
            "DataStreamProcessor": 0.25,
            "CloudResourceOptimizer": 0.20,
            "EdgeComputingManager": 0.15
        }
        
    def generate_status_report(self):
        active_tasks = self.get_active_tasks()
        project_status = self.get_project_status()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "active_tasks_count": len(active_tasks),
            "project_status": project_status,
            "overall_health": "good",
            "needs_attention": [
                proj for proj, status in project_status.items()
                if status < 0.3
            ]
        }
        
        return report
        
    def display_report(self, report):
        print("\n=== Project Coordination Report ===")
        print(f"Generated at: {report['timestamp']}")
        print(f"\nActive Tasks: {report['active_tasks_count']}")
        print("\nProject Status:")
        for proj, status in report['project_status'].items():
            print(f"- {proj}: {status*100:.1f}%")
        print("\nNeeds Attention:")
        for proj in report['needs_attention']:
            print(f"- {proj}")
            
def main():
    coordinator = ProjectCoordinator()
    report = coordinator.generate_status_report()
    coordinator.display_report(report)
    
if __name__ == "__main__":
    main()
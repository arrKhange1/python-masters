from dataclasses import dataclass
from typing import List

@dataclass
class TaskTracker:
    tasks = [
        { 'is_done': 1, 'description': 'Finished task', 'category': 'pstu'},
        { 'is_done': 0, 'description': 'Not finished task', 'category': 'work'},
        { 'is_done': 0, 'description': 'Yet another not finished task', 'category': 'work'},
    ]
    
    def print_tasks(self, ):
        for i, task in enumerate(self.tasks):
            print(f'{i+1}. [{'x' if task['is_done'] else ''}] {task['description']} #{task['category']}')
        

taskTracker = TaskTracker()
taskTracker.print_tasks()

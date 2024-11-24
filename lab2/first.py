from dataclasses import dataclass
import dataclasses
import json
import os
from typing import List, Optional

@dataclass
class Task:
    description: str
    category: str
    id: Optional[int] = None
    is_done: Optional[bool] = False

    def __getitem__(self, item):
        return getattr(self, item)

class TaskJsonManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def export_json(self, list_of_obj: List[Task]):
        jsonedTasks = json.dumps([dataclasses.asdict(obj) for obj in list_of_obj], sort_keys=True, indent=4)
        with open(self._file_name, 'w') as file:
            file.write(jsonedTasks)

    def import_json(self) -> List[Task]:
        if not os.path.isfile(self._file_name): return []
        with open(self._file_name, 'r') as file:
            return [Task(**obj) for obj in json.load(file)]

class TaskManager:
    tasks: List[Task] = []

    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def add(self, task: Task):
        new_task_id = self.tasks[-1]['id']+1 if len(self.tasks) else 1
        self.tasks.append(
            Task(
                description=task['description'],
                category=task['category'],
                is_done=0,
                id=new_task_id
            ))
    
    def remove(self, id: int):
        self.tasks = [task for task in self.tasks if task['id'] != id]

    def toggle_task_status(self, id: int):
        self.tasks = [Task(
                description=task['description'],
                category=task['category'],
                is_done= not task['is_done'],
                id=task['id']
            ) if task['id'] == id else task for task in self.tasks]
    
    def print_tasks(self):
        if len(self.tasks) == 0:
            print('--- No tasks ---')
            return
        for task in (self.tasks):
            print(f'{task['id']}. [{'x' if task['is_done'] else ''}] {task['description']} #{task['category']}')

class TaskTracker:
    taskManager: TaskManager
    jsonManager: TaskJsonManager

    def __init__(self):
        self.jsonManager = TaskJsonManager('tasks.json')
        tasks_from_json = self.jsonManager.import_json()
        self.taskManager = TaskManager(tasks_from_json)

    def start(self):
        while(True):
            self.taskManager.print_tasks()
            print('\nOptions:\n1. Add task\n2. Remove task\n3. Export as JSON\n4. Toggle task status\n5. Quit')
            match input('Enter desired option: \n'): 
                case '1':
                    self.taskManager.add(
                        Task(description=input('Enter task description: '), category=input('Enter task category: '))
                    )
                case '2':
                    self.taskManager.remove(int(input('Enter id of a task to be removed: ')))
                case '3':
                    self.jsonManager.export_json(self.taskManager.get_tasks())
                case '4':
                    self.taskManager.toggle_task_status(int(input('Enter task ID to toggle its status: ')))
                case '5':
                    print('Task Tracker finished work')
                    return

taskTracker = TaskTracker()
taskTracker.start()


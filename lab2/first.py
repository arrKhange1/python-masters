import json
import os
from typing import List, Dict

class JsonManager:

    file_name = 'tasks.json'

    def export_json(self, tasks):
        jsonedTasks = json.dumps(tasks, sort_keys=True, indent=4)
        with open(self.file_name, 'w') as file:
            file.write(jsonedTasks)

    def import_json(self):
        if not os.path.isfile(self.file_name): return []
        with open(self.file_name, 'r') as file:
            return json.load(file)

class TaskManager:
    tasks: List[Dict[str, any]] = []

    def __init__(self, tasks):
        self.tasks = tasks

    def get_tasks(self):
        return self.tasks

    def add(self, task):
        new_task_id = self.tasks[-1]['id']+1 if len(self.tasks) else 1
        self.tasks.append({**task, 'is_done': 0, 'id': new_task_id})
    
    def remove(self, id):
        self.tasks = [task for task in self.tasks if task['id'] != id]

    def toggle_task_status(self, id):
        self.tasks = [{**task, 'is_done': not task['is_done']} if task['id'] == id else task for task in self.tasks]
    
    def print_tasks(self):
        if len(self.tasks) == 0:
            print('--- No tasks ---')
            return
        for task in (self.tasks):
            print(f'{task['id']}. [{'x' if task['is_done'] else ''}] {task['description']} #{task['category']}')

class TaskTracker:
    taskManager: TaskManager
    jsonManager: JsonManager

    def __init__(self):
        self.jsonManager = JsonManager()
        tasks_from_json = self.jsonManager.import_json()
        self.taskManager = TaskManager(tasks_from_json)

    def start(self):
        while(True):
            self.taskManager.print_tasks()
            print('\nOptions:\n1. Add task\n2. Remove task\n3. Export as JSON\n4. Toggle task status\n5. Quit')
            match input('Enter desired option: \n'): 
                case '1':
                    self.taskManager.add({
                            'description': input('Enter task description: '), 
                            'category': input('Enter task category: ')})
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


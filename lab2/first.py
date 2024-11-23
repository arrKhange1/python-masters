from typing import List, Dict, Any


class TaskManager:
    tasks: List[Dict[str, any]] = [
    ]

    def add(self, task):
        new_task_id = self.tasks[-1]['id']+1 if len(self.tasks) else 1
        self.tasks.append({**task, 'is_done': 0, 'id': new_task_id})
    
    def remove(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]

    def toggle_task_status(self, id):
        self.tasks = [{**task, 'is_done': not task['is_done']} if task['id'] == id else task for task in self.tasks]
    
    def print_tasks(self):
        if len(self.tasks) == 0:
            print('--- No tasks ---')
            return
        for i, task in enumerate(self.tasks):
            print(f'{i+1}. [{'x' if task['is_done'] else ''}] {task['description']} #{task['category']}')

class TaskTracker:
    taskManager = TaskManager()

    def start(self):
        while(True):
            self.taskManager.print_tasks()
            print('\nOptions:\n1. Add task\n2. Export as JSON\n3. Toggle task status\n4. Quit')
            match input('Enter desired option: \n'): 
                case '1':
                    self.taskManager.add({
                            'description': input('Enter task description: '), 
                            'category': input('Enter task category: ')})
                case '2':
                    self.taskManager.export_as_json()
                case '3':
                    self.taskManager.toggle_task_status(int(input('Enter task ID to toggle its status: ')))
                case '4':
                    print('Task Tracker finished work')
                    return

taskTracker = TaskTracker()
taskTracker.start()


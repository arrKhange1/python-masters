class TaskManager:
    tasks = [
        { 'is_done': 1, 'description': 'Finished task', 'category': 'pstu'},
        { 'is_done': 0, 'description': 'Not finished task', 'category': 'work'},
        { 'is_done': 0, 'description': 'Yet another not finished task', 'category': 'work'},
    ]

    def add(self, task):
        self.tasks.append(task)
    
    def remove(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]
    
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
            print('\nOptions:\n1. Add task\n2. Export as JSON\n3. Print tasks')
            match int(input('Enter desired option: \n')): 
                case 1:
                    self.taskManager.add({
                            'is_done': 0,
                            'description': input('Enter task description: '), 
                            'category': input('Enter task category: ')})
                case 2:
                    self.taskManager.export_as_json()

taskTracker = TaskTracker()
taskTracker.start()


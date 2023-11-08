class TaskManagement:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id, title, description):
        task = Task(task_id, title, description, "To Do")
        self.tasks.append(task)

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status

    def list_tasks(self):
        for task in self.tasks:
            print(f"Task ID: {task.task_id}, Title: {task.title}, Status: {task.status}")

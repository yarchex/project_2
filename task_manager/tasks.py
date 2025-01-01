from task_manager.utils.validation import validate_priority, validate_date
from task_manager.exceptions import TaskNotFoundError

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self, title, description, priority, deadline):
        if not validate_priority(priority):
            print("Неверный приоритет. Используйте: низкий, средний, высокий.")
            return
        if not validate_date(deadline):
            print("Неверный формат даты. Используйте YYYY-MM-DD.")
            return
        task = {
            "id": self.task_id_counter,
            "title": title,
            "description": description,
            "priority": priority,
            "deadline": deadline,
            "status": "в процессе"
        }
        self.tasks.append(task)
        self.task_id_counter += 1
        print("Задача добавлена!")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print("Задача удалена!")
                return
        raise TaskNotFoundError(f"Задача с ID {task_id} не найдена.")

    def update_task(self, task_id, title=None, description=None, priority=None, deadline=None, status=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if title:
                    task["title"] = title
                if description:
                    task["description"] = description
                if priority and validate_priority(priority):
                    task["priority"] = priority
                if deadline and validate_date(deadline):
                    task["deadline"] = deadline
                if status:
                    task["status"] = status
                print("Задача обновлена!")
                return
        raise TaskNotFoundError(f"Задача с ID {task_id} не найдена.")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        for task in self.tasks:
            print(f"ID: {task['id']}, Название: {task['title']}, Описание: {task['description']}, "
                  f"Приоритет: {task['priority']}, Срок: {task['deadline']}, Статус: {task['status']}")

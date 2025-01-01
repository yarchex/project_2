from task_manager.tasks import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Изменить задачу")
        print("4. Просмотреть задачи")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            title = input("Название задачи: ")
            description = input("Описание: ")
            priority = input("Приоритет (низкий, средний, высокий): ")
            deadline = input("Срок выполнения (YYYY-MM-DD): ")
            manager.add_task(title, description, priority, deadline)
        elif choice == "2":
            task_id = int(input("ID задачи для удаления: "))
            manager.delete_task(task_id)
        elif choice == "3":
            task_id = int(input("ID задачи для изменения: "))
            print("Оставьте поле пустым, если не хотите изменять параметр.")
            title = input("Новое название задачи: ")
            description = input("Новое описание: ")
            priority = input("Новый приоритет (низкий, средний, высокий): ")
            deadline = input("Новый срок выполнения (YYYY-MM-DD): ")
            status = input("Новый статус (в процессе, завершено): ")
            manager.update_task(task_id, title, description, priority, deadline, status)
        elif choice == "4":
            manager.view_tasks()
        elif choice == "5":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

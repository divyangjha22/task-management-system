from services.user_service import User_Service
from services.task_service import Task_Service

def main():
    # Initialize services
    user_service = User_Service()
    task_service = Task_Service()

    print("--- User Service Demo ---")
    # Add a user
    new_user = user_service.add_users(1, "Divyang Jha", "divyangjha22@gmail.com")
    print(f"User added: {new_user.name} (Email: {new_user.email})")

    # Retrieve and display the same user using get_user()
    retrieved_user = user_service.get_user(1)
    if retrieved_user:
        print(f"Retrieved User: {retrieved_user.name} (Email: {retrieved_user.email})")
    else:
        print("User not found!")

    print("\n--- Task Service Demo ---")
    # Create tasks
    task1 = task_service.create_task(1, "Python Project Structure", "Understand the Python Project Structure")
    task2 = task_service.create_task(2, "Task Management System", "Create a Task Management System using Python")
    task3 = task_service.create_task(3, "Upload project", "Upload the project on Github")
    
    print("Tasks Created:")
    for task in [task1, task2, task3]:
        print(f"  Task {task.id}: {task.title} - {task.description}")

    # Complete tasks one by one and display results
    print("\nCompleting Tasks:")
    for i in range(3):
        result = task_service.complete_task()
        if result:
            task_id, title, description = result
            print(f"  Completed Task: {task_id} - {title}")
        else:
            print("  No more tasks to complete.")

    # Display task history using the stack
    print("\nTask History (Most Recent Completed First):")
    history = task_service.get_task_history()
    while not history.is_empty():
        task = history.pop()
        print(f"  Task {task.id}: {task.title} - {task.description}")

if __name__ == "__main__":
    main()

# import os
#
# FILE = "task.txt"
#
# # Load tasks from file
# def load_tasks():
#     if not os.path.exists(FILE):
#         return []
#     with open(FILE, "r") as f:
#         return [line.strip() for line in f]  # strip \n
#
# # Save tasks to file
# def save_tasks(tasks):
#     with open(FILE, "w") as f:
#         for t in tasks:
#             f.write(t + "\n")
#
# # Show tasks
# def show_tasks(tasks):
#     if not tasks:
#         print("No tasks found.")
#     else:
#         for i, t in enumerate(tasks, 1):
#             print(f"{i}. {t}")
#
# def main():
#     tasks = load_tasks()
#
#     while True:
#         print("\n1. View tasks")
#         print("2. Add task")
#         print("3. Mark task as done")
#         print("4. Delete task")
#         print("5. Exit")
#
#         choice = input("Choice: ").strip()
#
#         if choice == "1":
#             show_tasks(tasks)
#
#         elif choice == "2":
#             new_task = input("Enter new task: ").strip()
#             if new_task:
#                 tasks.append("[ ] " + new_task)
#                 save_tasks(tasks)
#                 print("Task added!")
#
#         elif choice == "3":
#             show_tasks(tasks)
#             try:
#                 num = int(input("Enter task number to mark done: "))
#                 if 1 <= num <= len(tasks):
#                     if tasks[num-1].startswith("[ ]"):
#                         tasks[num-1] = tasks[num-1].replace("[ ]", "[✔]", 1)
#                         save_tasks(tasks)
#                         print("Task marked as done!")
#                     else:
#                         print("Task already done.")
#                 else:
#                     print("Invalid task number.")
#             except ValueError:
#                 print("Enter a valid number.")
#
#         elif choice == "4":
#             show_tasks(tasks)
#             try:
#                 num = int(input("Enter task number to delete: "))
#                 if 1 <= num <= len(tasks):
#                     tasks.pop(num-1)
#                     save_tasks(tasks)
#                     print("Task deleted!")
#                 else:
#                     print("Invalid task number.")
#             except ValueError:
#                 print("Enter a valid number.")
#
#         elif choice == "5":
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Try again.")
#
# if __name__ == "__main__":
#     main()

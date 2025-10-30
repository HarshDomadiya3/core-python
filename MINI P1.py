# subject={"math", "science", "english"}
# class Student:
#     def __init__(self,roll_no,name):
#         self.info=(roll_no,name)
#         self.mark={}
#     def add_mark(self):
#         for sub in subject:
#             self.mark[sub] = int(input(f"Enter Mark For {sub}: "))
#     def display(self):
#         print(f"Roll No: {self.info[0]}, Name: {self.info[1]}")
#         for sub, mark in self.mark.items():
#             print(f"{sub}: {mark}")
#         avg = sum(self.mark.values()) / len(self.mark)
#         print(f"Percentage: {avg:.2f}%\n")
#
# students_list = []
#
# # Menu loop
# while True:
#     print("\n--- Student Management ---")
#     print("1. Add Student")
#     print("2. Show All Students")
#     print("3. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name = input("Enter student name: ")
#         roll_no = input("Enter roll number: ")
#         student=Student(roll_no,name)
#         student.add_mark()
#         students_list.append(student)
#     elif choice == "2":
#         for student in students_list:
#             student.display()
#     elif choice == "3":
#         break
#     else:
#         print("Invalid Choice")
#
#
#
#
#
#

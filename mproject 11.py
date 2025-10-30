# class Student:
#     def  __init__(self,name,roll_no,marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def percentage(self):
#         return sum(self.marks.values())/len(self.marks)
#     def results(self):
#         for m in self.marks.values():
#             if m <33:
#                 return "fail"
#         return "pass"
#     def show_results(self):
#         print("\n---- Student Result ----")
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         for subjects,mark in self.marks.items():
#             print(subjects,":", mark)
#         print("Percentage:", self.percentage(), "%")
#         print("Result:", self.results())
# name = input("Enter your name: ")
# roll_no = input("Enter your roll no: ")
#
# marks={}
# subject=["math","science","english"]
# for s in subject:
#     a=int(input("enter mark in subject"))
#     marks[s] = a
# student = Student(name, roll_no, marks)
# student.show_results()
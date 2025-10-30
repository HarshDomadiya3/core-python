# l=[]
# while True:
#     print("\n----To Do List Menu----")
#     print("1.Show tash")
#     print("2.Add task")
#     print("3.Delete task")
#     print("4.Exit")
#     choice=input("Enter your choice:-")
#     if choice=="1":
#         if len(l)==0:
#             print("No Task In List")
#         else:
#             print(l)
#     elif choice=="2":
#         b=int(input("Add Your Task:-"))
#         l.append(b)
#         print(l)
#     elif choice=="3":
#         if len(l)==0:
#             print("No Task In List")
#         else:
#             d=int(input("Delete Your Task:-"))
#             if d in l:
#                 l.remove(d)
#             print(l)
#     elif choice=="4":
#         print("Exit")
#         break

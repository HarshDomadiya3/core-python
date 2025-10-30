# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     if b==0:
#         raise ZeroDivisionError
#     return a/b
# def calculater():
#     while True:
#         print("welcome to calculator")
#         print("1.addiction")
#         print("2.subtraction")
#         print("3.multiplication")
#         print("4.division")
#         print("5.exit")
#         choice=input("enter your choice:-")
#         if choice in ["1","2","3","4"]:
#             a=int(input("enter first number:-"))
#             b=int(input("enter your second number:-"))
#             if choice=="1":
#                 print("addiction is",add(a,b))
#             elif choice=="2":
#                 print("subtraction is",sub(a,b))
#             elif choice== "3":
#                 print("multiplication is",mul(a,b))
#             elif choice=="4":
#                 print("division is",div(a,b))
#         elif choice=="5":
#             print("thank you")
#             break
#         else:
#             print("invalid choice")
# calculater()
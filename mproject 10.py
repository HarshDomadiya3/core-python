# class Atm:
#     def __init__(self,balance):
#         self.balance=balance
#     def check_balance(self):
#         print("your current balance is:",self.balance)
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print(amount,"deposit successfully")
#         else:
#             print("invalid amount")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("insufficient balance")
#         elif amount<0:
#             print("invalid amount")
#         else:
#             self.balance-=amount
#             print(amount,"withdraw successfully")
# atm=Atm(1000)
# while True:
#     print("\n-----ATM MENU-----")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")
#     choice=input("Enter your choice:")
#     if choice=="1":
#         atm.check_balance()
#     elif choice=="2":
#         amount=int(input("Enter amount:"))
#         if amount>0:
#             atm.deposit(amount)
#         else:
#             print("invalid amount")
#     elif choice=="3":
#         amount=int(input("Enter amount:"))
#         if amount<0:
#             print("invalid amount")
#         else:
#             atm.withdraw(amount)
#     elif choice=="4":
#         break
#
#
#
#
#
#

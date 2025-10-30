# class Account:
#     def __init__(self,acc_no,name,balance=0):
#         self.acc_no=acc_no
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print(f"Deposited{amount}.new balance={self.balance}")
#         else:
#             print("deposite valid amount")
#     def withdrow(self,amount):
#         if amount>0:
#             self.balance-=amount
#             print(f"withdrow{amount}.new balance={self.balance}")
#         else:
#             print("withdrow valid amount")
#     def display(self):
#         print(f"Account No:{self.acc_no} Name:{self.name} Balance:{self.balance}")
# class SavingAccount(Account):
#     def __init__(self,acc_no,name,balance,intrest_rate):
#         super().__init__(acc_no,name,balance)
#         self.intrest_rate=intrest_rate
#     def intrest(self):
#         intrest_rate=self.balance*intrest_rate/100
#         print(f"intrest earned:{intrest}")
#         return intrest
#
# account=[]
# while True:
#     print("\n===== Bank Management System =====")
#     print("1. Create Saving Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Calculate Interest")
#     print("5. Display Account")
#     print("6. Exit")
#
#     choice = input("Enter your choice: ")
#     if choice=="1"
#         acc_no=int(input("Enter Account No: "))
#         name=input("Enter Name: ")
#         balance=float(input("Enter Balance: "))
#         intrest_rate=float(input("Enter Interest Rate: "))
#         acc=Account(acc_no,name,balance)





#
#     # Parent Class
# class Account:
#     def __init__(self, acc_no, name, balance=0):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New Balance = {self.balance}")
#         else:
#             print("Enter valid amount!")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Balance!")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New Balance = {self.balance}")
#
#     def display(self):
#         print(f"Account No: {self.acc_no}")
#         print(f"Name      : {self.name}")
#         print(f"Balance   : {self.balance}")
#
#
# # Child Class (Savings Account)
# class SavingAccount(Account):
#     def __init__(self, acc_no, name, balance, interest_rate):
#         super().__init__(acc_no, name, balance)
#         self.interest_rate = interest_rate
#
#     def calcaccounts = []  # List to store accounts
#
# while True:
#     print("\n===== Bank Management System =====")
#     print("1. Create Saving Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Calculate Interest")
#     print("5. Display Account")
#     print("6. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         acc_no = input("Enter Account Number: ")
#         name = input("Enter Name: ")
#         balance = float(input("Enter Initial Balance: "))
#         interest_rate = float(input("Enter Interest Rate (%): "))
#         acc = SavingAccount(acc_no, name, balance, interest_rate)
#         accounts.append(acc)
#         print("Account Created Successfully!")
#
#     elif choice == "2":
#         acc_no = input("Enter Account Number: ")
#         amount = float(input("Enter Amount to Deposit: "))
#         for acc in accounts:
#             if acc.acc_no == acc_no:
#                 acc.deposit(amount)
#                 break
#         else:
#             print("Account not found!")
#
#     elif choice == "3":
#         acc_no = input("Enter Account Number: ")
#         amount = float(input("Enter Amount to Withdraw: "))
#         for acc in accounts:
#             if acc.acc_no == acc_no:
#                 acc.withdraw(amount)
#                 break
#         else:
#             print("Account not found!")
#
#     elif choice == "4":
#         acc_no = input("Enter Account Number: ")
#         for acc in accounts:
#             if acc.acc_no == acc_no:
#                 acc.calculate_interest()
#                 break
#         else:
#             print("Account not found!")
#
#     elif choice == "5":
#         acc_no = input("Enter Account Number: ")
#         for acc in accounts:
#             if acc.acc_no == acc_no:
#                 acc.display()
#                 break
#         else:
#             print("Account not found!")
#
#     elif choice == "6":
#         print("Exiting...")
#         break
#
#     else:
#         print("Invalid Choice! Try Again.")ulate_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         print(f"Interest earned: {interest}")
#         return interest
#
#
# # ===== Menu-driven System =====



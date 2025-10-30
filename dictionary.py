# Dict = mutable, unindexed, duplicate keys are not allowed
from enum import nonmember

# dic={
#     "name":"harsh",
#     "age":22,
# }
# print(dic)

# dic={
#      "name":"harsh",
# }
# print(dic.get("name"))

# dic={
#     "name":"harsh"
# }
# print(dic.keys())

# dic={
#     "name":"harsh"
# }
# print(dic.values())

# dic={
    # "name":"harsh"
# }
# print(dic.items())

# dic={
#     "name":"harsh"
# }
# dic.update({"name":"domadiya"})
# print(dic)

# dic={
#     "name":"harsh"
# }
# name=dic.pop("name")
# print(name)

# dic={
#     "name":"harsh",
#     "age":26
# }
# popitem=dic.popitem()
# print(popitem)

# dic={
#     "name":"harsh",
# }
# dic.clear()
# print(dic)

# update

# dic={
#     "student":"harsh",
#     "mark":25
# }
# dic.update(mark=45)
# print(dic)

# add key and value

# dic={
#     "apple":"10",
#     "banana":"20",
#     "orange":"30",
# }
# dic["grape"]=7
# print(dic)

# remove key and value

# dic={
#     "apple":"apple",
#     "banana":"banana",
#     "orange":"orange",
# }
# del dic["banana"]
# print(dic)

# average of given value

# dir={
#     "1":{"name":"harsh","math":88,"science":55}
# }
# for key,value in dir.items():
#     name=value["name"]
#     math=value["math"]
#     science=value["science"]
#     ave=(math+science)/2
# print(ave)

# dir ={
#     "1":{"name":"harsh","science":45},
#     "2":{"name":"raj","science":5},
#     "3":{"name":"shan","science":89},
# }
# top=None
# highest=-1
# for i in dir.values():
#     if i["science"]>highest:
#         height=i["science"]
#         top =i["name"]
# print(top)

# merge two  dictionary
# d={
#     "a":1
# }
# c={
#     "b":2
# }
# a=d|c
# print(a)

# merge two dictionary

# d={
#     "a":1
# }
# c={
#     "b":2
# }
# d.update(c)
# print(d)

# dictionary comprehension one line code

# s={"a":1,"b":2}
# print(s)

# check key is exists
# d={"a":1}
# if "a" in d:
#     print("yes")
# else:
#     print("no")

# class BankAccount:
#     def __init__(self, account_number, holder_name, balance=0.0):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ${amount:.2f} to account {self.account_number}.")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive.")
#         elif amount > self.balance:
#             print(f"Insufficient funds in account {self.account_number}.")
#         else:
#             self.balance -= amount
#             print(f"Withdrew ${amount:.2f} from account {self.account_number}.")
#
#     def display_balance(self):
#         print(f"Account {self.account_number} | Holder: {self.holder_name} | Balance: ${self.balance:.2f}")
#
#
# # --- Example Usage ---
#
# # Create two bank accounts
# account1 = BankAccount("123456789", "Alice Smith", 1000.0)
# account2 = BankAccount("987654321", "Bob Johnson", 500.0)
#
# # Perform transactions on account1
# account1.display_balance()
# account1.deposit(200)
# account1.withdraw(150)
# account1.withdraw(2000)  # should show insufficient funds
# account1.display_balance()
#
# print()
#
# # Perform transactions on account2
# account2.display_balance()
# account2.deposit(1000)
# account2.withdraw(300)
# account2.display_balance()


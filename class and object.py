# Class:- A class is like a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) of the object.
# Object:- An object is an instance of a class. Once a class is defined, you can create multiple objects from it.
# constructor :- constructor  means it's a special member function which calls whenever object create of the class,constructor is identity by __(underscore)
#              -- __init__ :- this function is call constructor in python and is called whenever the object is create of the class
from tkinter.font import names


# Class – Blueprint/template
#
# Object – Instance of a class
#
# Constructor (__init__) – Initializes the object
#
# Attributes – Variables tied to the object
#
# Methods – Functions tied to the object
#
# self – Refers to the current instance

# class name:
#     x="harsh"
# a=name()
# print(a.x)

# calling a function by object
# class name:
#     def function(self):
#         return "hellow"
# a=name()
# print(a.function())


# constructor(__init__),call it self it means dont nead to call(print) object,dont use return in __init__.

# class name:
#     def __init__(self):
#         print("hellow")
# a=name()

# class person:
#     def __init__(self,age):
#         self.age=age
#         if self.age>18:
#             print("You are young")
#         else:
#             print("You are not")
# a=person(19)


# class person:
#     def __init__(self,name):
#         self.name=name
# a=person("h")
# print(a.name)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         if self.age>18:
#             print("adult")
#         else:
#             print("minor")
# c=input("enter name")
# d=int(input("enter age"))
# a=person(c,d)

# class person:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
#     def display(self):
#         return self.first+" "+self.last
# a=person("Harsh","Domadiya")
# print(a.display())

# class person:
#     def __init__(self,name="harsh"):
#         self.name=name
# a=person()
# print(a.name)
# b=person("domu")
# print(b.name)

# Multiple Objects with Class Method
# Create a class BankAccount with attributes: account_number, holder_name, and balance.
# Add methods: deposit(), withdraw(), and display_balance().
# Create two bank accounts and perform various transactions.


# class bankaccount:
#         def __init__(self,account_number,holder_name,balance=0.0):
#             self.account_number=account_number
#             self.holder_name=holder_name
#             self.balance=balance
#         def deposit(self,amount):
#             if amount>0:
#                 self.balance+=amount
#                 # print(self.account_number)
#             else:
#                 print("positive")
#         def withdraw(self,amount):
#             if amount<0:
#                 print("amount must be positive")
#             elif amount>self.balance:
#                 print("Insufficient funds in account ")
#             else:
#                 self.balance-=amount
#                 # print(self.account_number)
#         def display_balance(self):
#             print(self.balance)
# account1=bankaccount(7433022609,"harsh",0)
# account1.deposit(1000)
# account1.withdraw(100)
# print(account1.balance)


# Create a class Student with attributes: name, roll_number, and grade.
# Create 3 student objects and print their details.

# class Student:
#     def __init__(self,name,roll_no,grade):
#         self.name=name
#         self.roll_no=roll_no
#         self.grade=grade
#     def display(self):
#         print(self.name,self.roll_no,self.grade)
# a=Student("harsh",22,"A")
# b=Student("domu",23,"b")
# c=Student("parth",24,"c")
# a.display()
# b.display()
# c.display()


# Method in Class
# Create a class Circle with an attribute radius.
# Add a method area() that returns the area of the circle. Create a circle object and print its area.


# import math
#
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
# a=circle(10)
# print(a.area())


# Constructor Usage
# Define a class Book with attributes: title, author, price.
# Use a constructor to initialize these values.
# Create two book objects and display their details.


# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def display(self):
#         print(self.title,self.author,self.price)
# a=Book("python","harsh",0)
# a.display()

# Modify Object Attributes
# Create a class Employee with name, position, and salary.
# Add a method promote() that increases salary and updates position.
# Create an employee object, promote them, and show the changes.

# class Employee:
#     def __init__(self,name,position,salary):
#         self.name=name
#         self.position=position
#         self.salary=salary
#     def promote(self,newposition,newsalary):
#         self.position=newposition
#         self.salary+=newsalary
#     def display(self):
#         print(self.name,self.position,self.salary)
# a=Employee("A","fresher",1000)
# a.display()
# a.promote("senior",10000)
# a.display()


# Object Interaction
# Create two classes: Author and Book.
# Each Book should have an Author object as an attribute.
# Display book details including author name.

# class Author:
#     def __init__(self,name):
#         self.name=name
# class book:
#     def __init__(self,author,price):
#         self.author=author
#         self.price=price
#     def display(self):
#         print(self.author.name,self.price)
# a=Author("harsh")
# b=book(a,100)
# b.display()

# List of Objects
# Create a class Product with id, name, and price.
# Store multiple product objects in a list and print products with price > 100.

# class product:
#     def __init__(self,id,name,price):
#         self.id=id
#         self.name=name
#         self.price=price
#     def display(self):
#         print(self.id,self.name,self.price)
# a=[
#     product(1,"python",200),
#     product(2,"py",90),
#     product(3,"c",9)
# ]
# for i in a:
#     if i.price>100:
#         i.display()

# Counting Instances
# Create a class Order and use a class variable to keep track of how many orders have been created.
# Each time an Order object is created, increment the counter.

# class order:
#     count=0
#     def __init__(self,id ,name):
#         self.id = id
#         self.name = name
#         order.count+=1
#     def display(self):
#         print(self.name,self.id)
# a=order(1,"python")
# b=order(2,"pyth")
# a.display()
# b.display()
# print(order.count)

# Static Methods
# Create a class MathUtils with static methods: add(), subtract(), multiply(), divide().
# Call these methods without creating an object.

# class static:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     @staticmethod
#     def sub(a,b):
#         return a-b
#     @staticmethod
#     def mul(a,b):
#         return a*b
#     @staticmethod
#     def div(a,b):
#         return a/b
# print(static.add(1,2))
# print(static.sub(1,2))
# print(static.mul(2,3))
# print(static.div(2,3))


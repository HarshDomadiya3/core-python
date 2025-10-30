# It is used to inherit the properties(attribute) and behaviours(method) of one class to another.(parent class to child class)

# 1)single inheritance:-
# 2)multilevel inheritance
# 3)multiple inheritance
# 4)hierarchical inheritance
# 5)hybrid inheritance

# 1) single inheritance:-
#        single inheritance  where a child class inherits attributes and methods from only one parent class.

# class parentclass:
#     def function1(self ):
#         print("parent class")
# class childclass(parentclass):
#     def function2(self ):
#         print("child class")
# a=childclass()
# a.function1()
# a.function2()


# Ek Parent class Account ho:
# Attributes: account_number, name, balance
# Method: display_account() jo account details print kare.
# Ek Child class SavingsAccount ho jo Account se inherit kare:
# Additional attribute: interest_rate
# Method: calculate_interest() jo balance par interest calculate karke print kare.


# class Account:
#     def __init__(self, account_number,name, balance):
#         self.account_number=account_number
#         self.name=name
#         self.balance=balance
#     def display(self):
#         print(self.account_number,self.name,self.balance)
# class saving_account(Account):
#     def __init__(self,account_number,name,balance,intrest_rate):
#         super().__init__(account_number,name,balance)
#         self.intrest_rate=intrest_rate
#         self.intrest=self.balance*intrest_rate/100

# a=saving_account(123,"harsh",10000,5)
# print(a.name,a.balance,a.intrest_rate)
# print(a.intrest)
#
# class Account:
#     def __init__(self,Acc_no,balance):
#         self.Acc_no=Acc_no
#         self.balance=balance
#         print("account_no",self.Acc_no)
#     def deposit(self,amount):
#         if amount<0:
#             print("enter valid balance")
#         else:
#             self.balance+=amount
#             print("deposit",self.balance)
#     def withdrawal(self,amount):
#         if amount>self.balance:
#             print("insufficient balance")
#         else:
#             self.balance-=amount
#             print("withdrawal",self.balance)
# class Saving_account(Account):
#     def __init__(self,Acc_no,balance,intrest_rate):
#         super().__init__(Acc_no,balance)
#         self.intrest_rate=intrest_rate
#     def intrest(self):
#         intrest=self.balance*self.intrest_rate/100
#         return intrest
#     def display(self):
#         print("total balance",self.balance)
# a=Saving_account(Acc_no=1,balance=0,intrest_rate=0.1)
# a.deposit(1000)
# a.withdrawal(100)
# a.display()

# class Library:
#     def __init__(self,library_name):
#         self.library_name=library_name
# class Book(Library):
#     def __init__(self,library_name,title,author,price):
#         super().__init__(library_name)
#         self.title=title
#         self.author=author
#         self.price=price
#     def display(self):
#         print(self.library_name,self.title,self.author,self.price)
# a=Book("lb","python","c",100)
# a.display()



# 2) multilevel inheritance
    # parent class ,sub parent class,child class


# class A:
#     def myfunction(self):
#         print("class A function called")
# class B(A):
#     def myfunction2(self):
#         print("class B function called")
# class C(B):
#     def myfunction3(self):
#         print("class C function called")
# a=C()
# a.myfunction()
# a.myfunction()
# a.myfunction2()


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class student(person):
#     def __init__(self,name,age,roll_no,grade):
#         super().__init__(name,age)
#         self.roll_no=roll_no
#         self.grade=grade
# class C(student):
#     def __init__(self,name,age,roll_no,grade,subject,marks):
#         super().__init__(name,age,roll_no,grade)
#         self.subject=subject
#         self.marks=marks
#     def display(self):
#         print(self.name,self.age,self.roll_no,self.grade,self.subject,self.marks)
# a=C("Harsh", 20, 101, "A", "Python", 95)
# a.display()



# 3) multiple inheritance
    # The Child class thus inherits the attributes and method from all parents


# class a1:
#     def function(self):
#         print('a1')
# class b2():
#     def function1(self):
#         print('b2')
# class c1(a1,b2):
#     def function3(self):
#         print('c1')
# a=c1()
# a.function()
# a.function1()
# a.function3()


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class employ:
#     def __init__(self,id,department):
#         self.id=id
#         self.department=department
# class details(Person,employ):
#     def __init__(self,name,age,id,department,salary):
#         Person.__init__(self,name,age)
#         employ.__init__(self,id,department)
#         self.salary=salary
#     def display(self):
#         print(self.name,self.age,self.id,self.department,self.salary)
# a=details("harsh",19,36,"it",0)
# a.display()


# 4) hierarchical inheritance
#         This type of inheritance contains multiple derived classes that are inherited from a single base class.

# class a1:
#     def function1(self):
#         print('a1')
# class a2(a1):
#     def function2(self):
#         print('a2')
# class a3(a1):
#     def function3(self):
#         print('a3')
# a=a2()
# a.function2()
# a.function1()
# a=a3()
# a.function1()
# a.function3()
# a=a1()
# a.function1()


# class vehicle:
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed
# class car(vehicle):
#     def __init__(self,name,speed,fule_type):
#         super().__init__(name,speed)
#         self.fule_type=fule_type
#     def display(self):
#         print(self.name,self.speed,self.fule_type)
# class bike(vehicle):
#     def __init__(self,name,speed,engin_capacity):
#         super().__init__(name,speed)
#         self.engin_capacity=engin_capacity
#     def display(self):
#         print(self.name,self.speed,self.engin_capacity)
# a=bike("A",10,100)
# a.display()
# a=car("B",20,"petrol")
# a.display()
# a=vehicle("C",30)
# print(a.name,a.speed)



# 5) hybrid inheritance
    # Combination of two or more types of inheritance is called as Hybrid Inheritance

# class b1:
#     def function1(self):
#         print('b1')
# class b2(b1):
#     def function2(self):
#         print('b2')
# class b3(b1):
#     def function3(self):
#         print('b3')
# class b4(b2,b3):
#     def function4(self):
#         print('b4')
# a=b4()
# a.function4()
# a.function2()
# a.function3()
# a.function1()


# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,rollno):
#         Person.__init__(self,name,age)
#         self.rollno=rollno
# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         Person.__init__(self,name,age)
#         self.subject=subject
# class Exam(Student, Teacher):
#     def __init__(self,name,age,rollno,subject,mark):
#         Student.__init__(self,name,age,rollno)
#         Teacher.__init__(self,name,age,subject)
#         self.mark=mark
#     def display(self):
#         print(self.name,self.age,self.rollno,self.subject,self.mark)
# a=Exam("harsh",26,36,"python",66)
# a.display()


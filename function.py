# A function is a block of code which run whe it called
# function is use for reusability of code
# A function is a block of code that performs a specific task.
# It takes input values, performs a series of operations, and produces an output value.

# types of functions:-

# 1) built in functions:
# 2)user-define functions:
# 3)lamda functions:

# 1) built in function

# -print()
# -range()
# -len()
# -round()
# -min()
# -max()

# 2) user define function

# def function():
#     return "harsh"
# print(function())

# function with one argument

# def function(a):
#     return a
# print(function(5))

# function with multiple arguments

# def function(a,b):
#     return a+b
# print(function(5,5))

# key word arguments ,print only given return argument

# def function(b1,b2,b3):
#     return b1
#print(function(5,6,4))

# default parameter value

# def function(harsh=1): # argument with perameter
#     return harsh
# print(function())

# def function(fruit):
#     for i in fruit:
#         print(i)
# a=["mango","apple","banana"]


# recursion function

# function(a)
# def function(x):
#     if x==1:
#         return 1
#     else:
#         return (x*function(x-1))
# x=int(input("enter number"))
# print(function(x))


# 3) lambda (anonymous) function

# a=lambda x:x*x
# print(a(5))


# a="mam"
# def function():
#     return a[::-1]
# print(function())

# factorial using function

# def fun(num):
#     fac=1
#     for i in range(1,num+1):
#         fac=fac*i
#     return fac
# num=(int(input("enter number")))
# print(fun(num))

# reverse string

# def fun(string):
#     return string[::-1]
# print(fun("python"))


# prime number or not prime

# def fun(num):
#     if num<2:
#         return "not prime"
#     for i in range(2,num):
#         if num%i==0:
#             return "not prime"
#     return "prime"
# while True:
#     num=int(input("enter number"))
#     print(fun(num))

# sum of given numbers

# def fun(num):
#     count = 0
#     for i in range(1,num+1):
#           count=count+i
#     return count
# print(fun(5))


# def fun(str):
#     word=str.split()
#     return len(word)
# print(fun("Hello world"))













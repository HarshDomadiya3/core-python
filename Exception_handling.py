# Exception handling in Python refers to managing runtime errors during the execution of a program

# two type of error
#     1)Syntax Error
#     2)Exception:-define int and add value string is Exception.

# Exception creating

# a=int(input("Enter a number"))
# b=0
# c=a/b
# print(c)

#solve single Exception creating

# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     c=a/b
#     print(c)
# except Exception as e:
#     print(e)
# print('A')

# Many exception

# try:
#     a=0
#     print(a)
# except Exception as e:
#     print(e)
# except:
#     print("exception")


# else with except

# try:
#     print("hello")
#     #print(a)
# except:
#     print("error")
# else:
#     print("nothing error")

# Finally block :-finally exception always print.

# try:
#      print("hellow")
#     #print(a)
# except:
#     print("error")
# finally:
#     print("finally")

# User define exceptions

# class exception(Exception):
#     pass
# c=10
# if c>5:
#     raise exception("ok")



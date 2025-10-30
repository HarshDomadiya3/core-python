# The range() function in Python generates an immutable sequence of numbers

# range(stop)
# range(start, stop)
# range(start, stop, step)


# sum of 1 to 100

# total=0
# for i in range(1,101):
#     total=total+i
# print(total)

# sum of even numbers

# a=0
# for i in range(1,101):
#     if i % 2==0:
#         a+=1
# print(a)


# Print the multiplication table of a given number

# num=int(input("enter a number"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)


# Count down from a given number to 0

# num=int(input("enter a number"))
# for i in range(num,-1,-1):
#     print(i)

#  print odd number

# for i in range(15,30):
#     if i%2 !=0:
#         print(i)

# factorial


# n=int(input("enter a number"))
# fac=1
# for i in range(1,n+1):
#     fac=fac*i
#     print(fac)

# Print all numbers between 1 and 50 that are divisible by both 3 and 4.

# for i in range(1,50):
#     if i %3==0 and i %4==0:
#         print(i)

# multiply of odd number

# a=1
# for i in range(1,11):
#     if i %2 !=0:
#         a*=i
# print(a)

# count of word

# str="harsh domadiya harsh domadiya"
# word=str.split()
# count={}
# for i in word:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i] = 1
# print(count)

# count of char

# str="harsh domadiya"
# count={}
# for i in str:
#     if i !=" ":
#         if i in count:
#             count[i]+=1
#         else:
#             count[i] = 1
# print(count)



# having same name but different signature
# function having same name but different signature
# Having many form of same name

# 1) compile time polymorphism
        # a) method overloading
#           same name methods in same class but different arguments
#           in method overloading inheritance not required
# 2) runtime polymorphism
#     a) method overriding
#           same name methods but different class argumemt are also same
#           in method overridig inheritance is compulsory


# method overloading

# class Mo:
#     def function(self):
#         print("mo function called")
#     def function(self,a):
#         print("function with one arguments")
#     def function(self,a,b):
#         print("function with two arguments")
#
# m=Mo()
# m.function(10,20)
# method overloading is not supported in python because python on interperted language

# method overriding

# class Mo1:
#     def myfunction(self):
#         print("Mo1 function")
# class Mo2(Mo1):
#     def myfunction(self,a):
#         print("Mo2 function")
#         super().myfunction()
# class Mo3(Mo2):
#     def myfunction(self,a):
#         print("Mo3 function")
#         super().myfunction(10)
# a=Mo3()
# a.myfunction(10)


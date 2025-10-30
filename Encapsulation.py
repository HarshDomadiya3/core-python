# variable and methods in singel entity(unit) its call Encapsulation
# _(single underscore)stand for protected
# __(double underscore)stand for private

# Private

# class Car:
#     def __init__(self, brand, speed):
#         self.__brand = brand     # private
#         self.__speed = speed     # private
#
#     def show(self):
#         print("Brand:", self.__brand, "Speed:", self.__speed)
#
#
# c = Car("BMW", 200)
# c.show()



# class A:
#     def __init__(self,a):
#         self.__a=a
#     def show(self):
#         print(self.__a)
# class B(A):
#     def __init__(self,b):
#         super().__init__(10)
#     def showB(self):
#         print(self.__a)
# a=B(10)
# a.show()


# Protect


# class Car:
#     def __init__(self, brand, speed):
#         self._brand = brand       # protected variable
#         self._speed = speed
#
#     def show(self):
#         print("Brand:", self._brand, "Speed:", self._speed)
#
# c = Car("Audi", 150)
# c.show()


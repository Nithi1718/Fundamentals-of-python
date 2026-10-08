# from abc import *
# class A:
#     # @abstractmethod
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
#
#     def log(self):
#         print(self.__c)
#
# class B(A):
#     def log3(self):
#         print(self.a)
#         # super().log()
#
# class C(B):
#     def log2(self):
#         print(self._b)
#         print(self.a)


# a=C(1,2,3)
# print(a._b)
# print(a.a)
# print(a._A__c)


# from abc import *
#
# class A(ABC):
#     @abstractmethod
#     def join(self):
#         pass
# class B(A):
#     def join(self):
#         print("Hi bro")
#     def join2(self):
#         print("Hello")
#
# class C(A):
#     def join3(self):
#         print("Showing")
#
# a=B()
# a.join2()


# from abc import ABC, abstractmethod
#
# class A():
#     # @staticmethod                       #Static method
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
#
#     def boy(self):
#         print("he is a boy")
#
# class B(A):
#     # @abstractmethod
#     def boy(self):                      #Dynamic method
#         print("Girl")
#
# class C(A):
#     def boy(self):
#         print("Lonely")
#         super().boy()                 # A is inherited in C.... super().boy()
#         print(self.a, self._b)


# a=C(1,2,3)
# a.boy()              #overloading not allowed in python
# a.boy()           #overriding is allowed


# class A:
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
#
#     def boy(self):
#         print("boy",self.a,self._b,self.__c)
# class B(A):
#     def girl(self):
#         print("girl",self.a,self._b)
#
# a=B(1,2,3)
# a.boy()
# a.girl()
# print(a._b)
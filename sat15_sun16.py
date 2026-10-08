### Encapsulation public protected private


# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def fun(self):
#         pass
#
# class B(A):
#     def fun(self,a):
#         print("Abstract method implemented")
#
# obj = B()
# obj.fun(22)


# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def fun(self):
#         pass
#     def fun3(self):
#         print("nothing inside")
#
# class C(A):
#     def fun(self):
#         pass
#     def fun3(self):
#         print("nothing bye")
#
# class B(C,A):
#     def fun(self):
#         pass
#     def fun2(self):
#         super().fun3()
#         print("Hey bro")
#         # super().fun2()
# c=B()
# c.fun2()

# class A:
#     def __init__(self,a,b,c):
#         self.a=a
#         self._b=b
#         self.__c=c
#     def pro(self):
#         print(self.a,self._b,self.__c)
# class B(A):
#     def drago(self):
#         print("Hey dude")
#         print(self.a,self._b)
#
# b=B(1,2,3)
# b.pro()
# b.drago()

#
# class A:
#     def __init__(self,a,_b,__c):
#         self.a=a
#         self._b=_b
#         self.__c=__c
#
#     def toby(self):
#         print(self.__c)
#
# class B:
#     def __init__(self,e,_f,g):
#         self.e=e
#         self._f=_f
#         self.__g=g
#
# class C(A,B):
#     def dummy(self):
#         print(self.a)
#         print(self.e)
#         print(self._b)
#
# a=C(3,"k","j")
#
# a.toby()
# a.dummy()

# from recall import (add, sub,mul, div)
# from recall import *
# import recall
# print(recall.add(2,3))

# from models.metrics.recall import *
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))
#
# from models.metrics.recall import add, sub,mul,div
# print(sub(2,3))
# print(add(5,6))
# print(mul(2,3))
# print(div(3,2))
#
# import models.metrics.recall
# print(models.metrics.recall.add(5,6))
# print(models.metrics.recall.sub(5,6))
# print(models.metrics.recall.mul(5,6))

# from nnnn import *
# c=C()
# c.log()


# numbers = [5, 2, 8, 1]
# a=reversed(numbers)
# print(a)

# def fun(*a):
#     print(max(a))
# fun(1,2,3,4)

# def fun(a,*b,c=3,**d):
#     print("add",a+c,"\n",max(b),"\n",d)
# fun(1,2,3,4,c=5,b=1,n=1)

# p=lambda a,b,c : (a,b,c)
# print(p(1,c=8,b=2))

from abc import *


class A:

    def __init__(self,a,b,c):
        self.a = a
        self._b = b
        self.__c = c
        print("sun", self.a, self._b, self.__c)

    def mon(self,n):
        print("mon", n)

class B(A):
    # @abstractmethod
    def tue(self):
        print(self.a, self._b, self._A__c)
        print("mon")

c=B(3,5,6)
c.mon(666)
c.tue()
print(c.a)
print(c._b)
print(c._A__c)



















































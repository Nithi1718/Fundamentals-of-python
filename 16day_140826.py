# # class A:
# #     def add(self,a,b):
# #         print(a+b)
# # class B(A):
# #     # @staticmethod
# #     def add(self,a,b):
# #         super().add (a,b)
# #         print(a-b)
# #
# # a=B()
# # a.add(1,2)
# # a.add(4,1)
#
#
# # class A:
# #     def add(self,a,b):
# #         print(a+b)
# #     def add(self):
# #         print("The function is end")
# #
# # class B(A):
# #
# #     def add(self,a,b):
# #         super().add(a,b)
# #         print("sub",a-b)
# # b=B()
# # b.add(1,2)
# #
# # class A:
# #     def add(self,a,b):
# #         print("add",a+b)
# #     def add(self,a,b):
# #         print("sub",a-b)
# #
# # c=A()
# # c.add(1,2)
#
#
# # from abc import ABC, abstractmethod
# #
# # class Payment(ABC):
# #
# #     @abstractmethod
# #     def nnn(self,amount):
# #         print("The amount is credited to your account, now your current bfank bank balance is 20000000000000")
# #         pass
# #
# # class UPI(Payment):
# #
# #     def nnn(self):
# #         print(f"Paid ₹{amount} using UPI")
# #
# #
# # class CreditCard(Payment):
# #
# #     def nnn(self, amount):
# #         super().nnn(amount)
# #         print(f"Paid ₹{amount} using Credit Card")
# #
# # upi = UPI()
# # upi.nnn(500)
# #
# # card = CreditCard()
# # card.nnn(1000)
#
#
#
# # class A:
# #     @staticmethod
# #     def add(a,b):
# #         print(a+b)
# # class B(A):
# #     def sub(self,a,b):
# #         print(a-b)
# #
# # a=B()
# # a.add(1,2)
# # a.sub(3,5)
#
#
#
#
# # class B:
# #     @staticmethod
# #     def add(a,b):
# #         print(a+b)
# #
# # class A(B):
# #     # @staticmethod
# #     def add(self,a,b):
# #         super().add(a,b)
# #         print(a-b)
# #
# # a=A()
# # a.add(1,2)
# # a.add(8,2)
#
#
# # from abc import ABC, abstractmethod
# #
# # class A(ABC):
# #     # @abstractmethod
# #     def sum(self,b):
# #         print(b)
# #         pass
# #
# # class B(A):
# #     def sum(self,b):
# #         print(f"The value is {b}")
# # a=B()
# # a.sum(2)
# #
# # a=A()
# # a.sum(5)
#
# # from abc import ABC, abstractmethod
# #
# # class Payment(ABC):
# #
# #     @abstractmethod
# #     def nnn(self,amount):
# #         print("The amount is credited to your account, now your current bfank bank balance is 20000000000000")
# #         pass
# #
# # class UPI(Payment):
# #
# #     def nnn(self,amount):
# #         print(f"Paid ₹{amount} using UPI")
# #
# #
# # class CreditCard(Payment):
# #
# #     def nnn(self, amount):
# #         super().nnn(amount)
# #         print(f"Paid ₹{amount} using Credit Card")
# #
# # upi = UPI()
# # upi.nnn(500)
# #
# # card = CreditCard()
# # card.nnn(1000)
#
# # from abc import ABC, abstractmethod
# #
# # class A(ABC):
# #     @abstractmethod
# #     def sum(self,b):
# #         print("Hi sorry bro")
# #         pass
# #
# # class B(A):
# #     def sum(self,b):
# #         print(f"The value is {b}")
# #
# # class C(A):
# #     def sum(self,b):
# #         super().sum(b)
# #         print("Nothing to say sorry bro")
# #
# # a=B()
# # a.sum(2)
# #
# # a=C()
# # a.sum(5)
#
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod           ### itha command pannitu call panni run panna answer varum otherwise varathu
#     def fun(self):
#         pass
#
# class B(A):
#     def fun(self,a):
#         print("The B")
#
# class C(A):
#     def fun(self,a):
#         print("The C")
#
#     def fun1(self,a):
#         print("The C is implemented")
#
# a=C()
# a.fun(4)
#
# # b=C()
# # b.fun(5)
#
#
# # class A:
# #     def __init__(self,a,b,c):
# #         self.a = a
# #         self._b = b
# #         self.__c = c
# # class B(A):
# #     def logoo(self):
# #         print("logo of B",self.__c)
# # b=B(2,3,4)
# # b.logoo()
# # # print(b._A__c)
#
#
#
#
#
#


a=7
if a<5:
    print('less')

if a<9:
    print('eligible')



























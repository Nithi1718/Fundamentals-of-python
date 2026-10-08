# a=1
# while a<=10:
#     a += 1
#     if a==4:
#         continue
#     print(a)



# for i in range(1,11):
#     if i==4:
#         continue
#     print(i)

# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\JJ.txt","r")
# print(a.read())
# a.close()

# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\JJ.txt",'w')
# a.write("I am 23")
# a.close()

# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\JJ.txt",'a')
# a.write("\t I am nithish")
# a.close()

# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\NN.txt",'x')
# a.write("I am Nithish Kumar and i am 23 years old")
# a.close()

# a=int(input("Enter the number: "))
# print("less") if a<5 else print("greater")

# a=6
# print("low") if a<7 else print("Equal") if a==7 else print("High")


# print("low") if a<7 else print("high")

# a=int(input("Enter the number: "))
# print("Fail") if a<30 else print("pass") if a<50 else print("average") if a<=70 else print("good")


# a=[i for i in range(1,11)]
# print(a)


# a=[]
# for i in range(1,11):
#     a.append(i)
# print(a)


# a=['nithi',23,52,171,"Team Lead"]
# a=[x for x in a]
# print(a)

### Shorthand if, List Comprehension, lambda, pass break continue

### lambda

# add=lambda a,b: a+b
# print(add(2,3))

# def logo(*d):

# a=input("Enter the word: ")
# if a==a[::-1]:
#     print("palindrome")

# sub=lambda a,b:b-a
# print(sub(2,6))

# for i in range(1,11):
#     if i==7:
#         continue
#     print(i)

# x=[i for i in range(1,19)]
# print(x)
#
# age=18
# print("child") if age<18 else print("adult") if age<25 else print("adult")

# a=lambda *d:sum(d)
# print(a(1,1,2,3,3,5,4,5,6,7,7,7,7))


# class Car:
#     def __init__(self, make, model, year): # constructor method
#         self.make = make #attribute declaration
#         self.model = model
#         self.year = year
#
#     def make_check(self): #method or function
#         if self.make == "Ford":
#             print("i like this car")
#         else:
#             print("i do not like this car")
#
#     def model_check(self):
#         if self.model in ['endeuar','hilux','brezza']:
#             print("i love this model")
#         else:
#             print("i do not like this model")
#
# Aravind = Car('Ford1','brezza',2026) # instance
# Aravind.make_check()
# Aravind.model_check()
#
# Vinoth = Car('BMW','X1',2025)
# Vinoth.make_check()
# Vinoth.model_check()


# a=[y for y in range(1,11)]
# print(a)
#
# c=[]
# for i in range(1,11):
#     c.append(i)
#
# print(c)

# a=int(input("Enter the age: "))
# print("he is child") if a<13 else print("he is adult") if a<25 else print("he is major"))


# a=int(input("Enter the age: "))
# if a<13:
#     print("He is child")
# elif a<25:
#     print("He is adult")
# else:
#     print("He is major")


# add=lambda *d:sum(d)
# print(add(1,2,3,4,5,6,7,8,9,10))

# def add(*d):
#     return sum(d)
# c=add(1,2,3,4,5,6,7,8,9,10)
# print(c)

# for x in range(1,6):
#     if x==3:
#         break
#
#     print(x)

### object attribute behaviour
























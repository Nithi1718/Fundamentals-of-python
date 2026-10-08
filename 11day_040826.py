### Return Function

## In return function we hold the value passes through the argument


# def dragon(a,b):
#     return(a+b)
# dragon(4,5)
#
# # print(2,3)                      ## Prints only (2,3) works as normal prints
#
# print(dragon(4,5))          ## prints the answer because we call our function
# c=dragon(4,10)              ## we call fucntion name
# print(c)




# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     print(a/b)
# except Exception as n:
#     print(n)
# # except TypeError:
# #     print("Type error")
# # except NameError:
# #     print("Name error")
# # except ZeroDivisionError:
# #     print("division error caused by  zero")
# # except ValueError:
# #     print("Value error occured")
# # except TypeError:
# #     print("Type Error")
# finally:
#
#     print("Thanky you for visiting")

# print(a+b)





# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\a.txt",'r')
#
#
# print("hello\nworld")

# a=[1,2,3,1,4,5]
# # print(a.count(1))
# # print(a.index(1,2))
# c=a.copy()
# a.pop()
# print(a)
# print(c)

# a={1,2,3,4}
# b={4,5,6}
# # a.add(4)
# # print(a)
# a.update(b)
# print(a)

# a={1,2,3,4}
# b={1,2,5,6,7}
# print(a)
# a.intersection_update(b)
# print(a)
# b.difference_update(a)
# print(b)

# print(a.symmetric_difference(b))
# a.symmetric_difference_update(b)
# print(a)
#
# a={1,2,3,4,5,6,7,8}
# b={1,2,3,4,5,6}
# c={1,2,10}
# a.discard(9)
# print(a)

# a=[1,2,3,4,1,2,3,4,5,6,5,6,7]
# c=[]
#
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)

### Error handling
## try:, except:, finally:,     except Exception as e:

# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\a.txt",'r')
# print(a.read())
# a.close()
#
# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\a1.txt",'w')
# a.write("Hello world")
# a.close()
#
# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\a.txt",'a')
# a.write("\nHello my world")
# a.close()
#
# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\a2.txt",'r')
# print(a.read())
# a.close()

# def logo(a,v):
#     for i in range(a,v,-1):
#         print(i)
#

# logo(1,10)
# logo(10,20)
# logo(10,1)

# a=[1,2,3,4,5]
# b=[2,3,6,7]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# a=[1,2,3,3,2,4,1]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]==a[j]:
#             print(a[i])

# a=[1,2,3,4,5,6,7]
# a.sort(reverse=True)
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]+a[j]==9:
#             print(a[i],a[j])

# a=[10,20,30,40]
# for x in range(len(a)):
#     for y in range(x+1, len(a)):
#         if a[x]!=a[y]:
#             print(a[x], a[y])
#
# a=0
# for i in range(1,6):
#     a+=i
#
# print(a)
#
# even=0
# odd=0
#
# for i in range(1,101):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)

# a=143
# b=0
#
# for i in str(a):
#     d=a%10
#     b=b*10+d
#     a=a//10
# print(b)
#
# a=1433
# b=0
# for i in str(a):
#     b+=int(i)
# print(b)

# for i in range(1,11):
#     if i%2==0:
#         print("*"*2)
#     else:
#         print("*"*1)

# a=5
# for i in range(1,a+1 ):
#     print(" "*(a-i)+"*"*((2*i)-1))
#
# a=5
# for i in range(a-1,0,-1):
#     print(" "*(a-i)+"*"*((2*i)-1))


# a=1
# while a<=10:
#     b=1
#     while b<=10:
#         print(f"{a}X{b}={a*b}")
#         b+=1
#     a+=1
#
# a=1
# b=5
# while a<=b:
#     print(" "*(b-a)+"*"*((2*a)-1))
#     a+=1
#
# a=4
# b=5
# while a>=1:
#     print(" "*(b-a)+"*"*((2*a)-1))
#     a-=1

# def logo(a,b):
#     return a+b, a-b
#
# sum, difference = logo(5,7)
# print(sum)
# print(difference)

# a=[1,2,3,4,5]
# b="B"
# print(dict.fromkeys(a,b))
#
# def add(**d):
#     print(d)
# add(x=1,y=2,z=3)
# add(name="nithi", age=23,weight=52, height=171)


# try:
#     a=10
#     b=0
#     print(a/c)
#     print(a/b)
# except Exception as e:
#     print(e)
# finally:
#     print("hi bro")
# a,b=10,2
# print(a/c)
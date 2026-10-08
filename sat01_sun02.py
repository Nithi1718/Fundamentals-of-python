# a={1,2,4,3}
# for i in a:
#     print(i)
#
# b={"name":"Nithish","age":23,"height":169,"weight":49,"role":"AI & ML"}
# for i in b.items():
#     print(i)
# for i in {"name":"Nithish","age":23,"height":169,"weight":49,"role":"AI & ML"}.items():
#     print(i)

# a="nithish"
# for i in a[::-1]:
#     print(i)

### STAR printing pattern

# for i in range(1,6,1):
#     print("*"*i)
# for i in range(5,0,-1):
#     print("*"*i)


# rows=10
# i=0
# while i<=rows:
#     print(" "*(rows-1),"*"*i)
#     i+=1
#     rows-=1

# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*i)

# a=1
# while a<=10:
#     print(a)
#     a+=1
#
# a=10
# while a>0:
#     print(a)
#     a-=1

# a=5
# for i in range(1,a+1):
#     print("*"*i)
#
# a=5
# for i in range(a,0,-1):
#     print("*"*i)
#
# a=5
# for i in range(1,a+1):
#     print(" "*(a-i)+"*"*i)
#
# a=5
# for i in range(a,0,-1):
#     print(" "*(a-i)+"*"*i)

# n=5
# for i in range(1,n):
#     print(" "*(n-i)+"*"*(2*i-1))
#     n = 5
# for i in range(n,0,-1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

#### printing for pyramid and diamond pattern

# n=5
# for x in range(1,n+1,1):
#     print(" "*(n-x)+"*"*((2*x)-1))
# # print()
# n=5
# for x in range(n-1,0,-1):
#     print(" "*(n-x)+"*"*((2*x)-1))

# n=5
# for i in range(1,n+1):
#     print("*"*i)
# for j in range(n-1,0,-1):
#     print("*"*j)
# print()
#
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+'*'*j)

# a=[1,2,3,4]
# b=[5,6,7,8]
#
# for i in a:
#    if i not in b:
#        print(i,b)

# a=[1,7,2,6,3,4,5]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==9:
#             print(a[j],a[i])

# a=1432
# b=0
# for i in str(a):
#    b+=int(i)
# print(b)


# a=1432
# c=str(a)
# for i in range(1):
#     print(c[::-1])


# a=1432
# d=0
# for i in str(a):
#     c=a%10
#     d=d*10 +c
#     a//=10
# print(d)

# a=1432
# b=0
# c=str(a)
# while b<=len(c):
#     b+=1
# print(c[::-1])

# a=1432
# b=-2
# c=0
# while b<=len(str(a)):
#     d=a%10
#     c=c*10+d
#     a//=10
#     b+=1
# print(c)

# ###  Addition using while loop
# a=1432
# b=0
# c=0
# d=str(a)
# while b<len(d):
#     c+=int(d[b])
#     b+=1
# print(c)

# a=1432
# b=0
# c=
# while a<=len(c)

# for i in range(1,11):
#     print(f"{2}X{i}={2*i}")

#
# for i in range(2,11):
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}",end="\t")
#     print("")

# a=1
# while a<=10:
#     b=1
#     while b<=10:
#         print(f"{a}X{b}={a*b}",end="\t")
#         b+=1
#     print()
#     a+=1

# a=1
# b=5
# while a<=b:
#     print("*"*a)
#     a+=1
#
# a=5
# b=1
# while a>=b:
#     print("*"*a)
#     a-=1
#
# a=1
# b=5
# while a<=5:
#     print(" "*(b-a)+"*"*a)
#     a+=1
# #
# a=1
# b=5
# c=5
# while a<=5:
#     print(" "*(c-b)+"*"*b)
#     a+=1
#     b-=1

# a=1
# c=5
# while a<=c:
#     print(" "*(c-a)+"*"*((2*a)-1))
#     a+=1
# a=1
# c=5
# b=5
# while a<=c:
#     print(" "*(c-b)+"*"*((2*b)-1))
#     a+=1
#     b-=1


##For loop
# c=5
# for i in range(1,c+1):
#     print(" "*(c-i)+"*"*((2*i)-1))
#
# c=5
# for i in range(c-1,0,-1):
#     print(" "*(c-i)+"*"*((2*i)-1))

# a=[1,2,3,4,5,2,1,3]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             print(a[i])

# a=[1,2,3,4]
# b=[5,2,6,3]
# c=[]
#
# for i in a:
#     if i not in b:
#         c.append(i)
# for j in b:
#     if j not in a:
#         c.append(j)
# print(c)


# a=[4,5,6,1,3,7,2]
# a.sort(reverse=True)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==9 and a[i]>a[j]:
#             print(a[i],a[j])


# a=[1,2,3,4]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]!=a[j]:
#             print(a[i],a[j])for


# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*(2*i-1))
#
# a=4
# n=1
# b=5
# while a>=n:
#     print(' '*(b-a)+"*"*(2*a-1))
#     a-=1
# print()
#
# a=1
# n=5
# while a<=n:
#     print(" "*(n-a)+"*"*(2*a-1))
#     a+=1

# a=4
# n=1
# b=5
# while a>=n:
#     print(" "*(b-a)+"*"*((2*a)-1))
#     a-=1
# print()

# n=5
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*((2*i)-1))

# a=1
# n=5
# while a<=n:
#     print("*"*a)
#     a+=1
#
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*(2*i-1))


# a=1
# n=5
# while a<=n:
#     print(" "*(n-a)+"*"*((2*a)-1))
#     a+=1
#
# a=4
# n=1
# b=5
# while a>=n:
#     print(" "*(b-a)+"*"*((2*a)-1))
#     a-=1


# a=[1,2,3,4]
# b=[2,3,5,6]

# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             # print(a[i])
#             print(b[j])

# a=[1,2,3,4]
# b=[2,3,5,6]
# c=[]
#
# for i in a:
#     if i not in b:
#         c.append(i)
# for j in b:
#     if j not in a:
#         c.append(j)
# print(c)


# a=[1,2,3,4,4,3,2,5,6,7,1]
# c=[]
#
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)


#### Printing uncommon elements from list a and list b
# a=[1,2,3,4]
# b=[5,6,2,3]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)
#
# for i in b:
#     if i in a:
#         c.append(i)
# print(c)

# for i in a:
#     for j in b:
#         if i==j:
#             print(i)

# a={True,2,3,4,"nithi"}
# print(a)
### For reversing the integer using the string we use some tricks and formula
### condition if a=integer and c=0 and d=a%10 c=c*10+d and finally add one condition that splits into 2
### a=a//10   ------- this helps to split the integer into 2 parts... second part has 1 element and
### the first part has remaining elements in a.. For running for the 2nd time the value of 'a' is updated




#a=143
# c=0
# for i in str(a):
#     c+=int(i)
# print(c)


# a=143
# c=0
# for i in str(a):
#     d=a%10
#     c=c*10+d
#     a=a//10
#     print(c)

# b=25572
# c=0
#
# for i in  str(b):
#    c+=(int(i))
#    print(c)
# for i in str (b):
#    d=b%10
#    c=c*10+d
#    b=b//10
#    print(c)


## While loop
# a=1
# while a<5:
#    print(a)
#    a+=1

# for i in range(1,11):
#    if i%2==0:
#       print(i)

# a=0
# while a<100:
#    if a%2==0:
#       print(a)
#    a+=1

# a=1
# while a<=10:
#    print(a)
#    a+=1

# b=10
# while b>=1:
#    print(b)
#    b-=1

# a=144
# b=0
# for i in str(a):
#    c=a%10
#    b=b*10+c
#    a=a//10     ###   or    a//=10
#    print(b)


# a=1
# while a<=10:
#    print(f"{2}X{a}={2*a}")
#    a+=1

# for i in range(1,11):
#    for j in range(1,11):
#       print(f"{i}X{j}={i*j}",end='\t')
#    print()

# a=1
# b=1
# while a<=10:
#    for b in range(1,11):
#       print(f"{a}X{b}={a*b}")
#       b+=1
#       a+=1

# a=1
# while a<=10:
#    print(f"{2}X{a}={a*2}")
#    a+=1

# a=143
# b=0
# for i in str(a):
#    c=a%10
#    b=b*10+c
#    a//=10
#    print(b)


# for i in str(a):
#    b+=int(i)
# print(b)


# a=143
# b=0
# for i in str(a):
#    b+=int(i)
#    print(b)

#
# a=143
# b=0
# x=0
# c=str(a)
# while x<=len(c):
#    d=a//10
#    b=b*10+d
#    a//=10
#    print(b)
#    x+=1

# a=1
# while a<=10:
#    print(f"{2}X{a}={2*a}")
#    a+=1

# a=10
# while a>=1:
#    print(a)
#    a-=1
#
# b=1
# while b<=10:
#    print(b)
#    b+=1


# a=143
# while a<=len(str(a)):


# a=[2,3,4,3,2,5,5]
# for i in range(len(a)):
#    for j in range(i+1, len(a)):
#       if a[i]==a[j]:
#          print(a[i])

# a=[10,20,30,30,40,40,10]
# for i in range(len(a)):
#    for j in range(i+1, len(a)):
#       if a[i]==a[j]:
#          print(a[i])

# a=[10,20,30,40]
# for i in range(len(a)):
#    for j in range(i+1, len(a)):
#       if a[i]!=a[j]:
#          print(a[i],a[j])

# i=1
# while i<=10:
#    j=1
#    while j<=10:
#       print(f"{j}X{i}={i*j}",end="\t")
#       j+=1
#    print()
#    i+=1

# a=1
# while a<=10:
#    print(f"{2}X{a}={2*a}")
#    a+=1

# a=10
# while a>=1:
#    print(a)
#    a-=1
#


# a=1
# while a<=10\
#         :
#    b=1
#    while b<=10:
#       print(f"{a}X{b}={a*b}", end='\t')
#       b+=1
#    print()
#    a+=1

# a=143
# b=-1
# c=0
# while b<=len(str(a)):
#    d=a%10
#    c=c*10+d
#    a=a//10
#    print(c)
#    b+=1


# a=143
# b=0
# c=0
# d=str(a)
# while b<len(str(a)):
#    c+=int(d[b])
#    print(c)
#    b+=1


# a=143
# c=0
# for i in str(a):
#    c=c+int(i)
#    print(c)

# b=0
# while b<=10:
#
#
#       a=int(input("Enter the marks between 1 and 100: "))
#       if a>0 and a<=100:
#          if a<30:
#             print("Fail")
#          elif a<60:
#             print("Pass")
#          elif a<80:
#             print("Average")
#          else:
#             print("Good")
#       else:
#          print("Invalid marks")
#
#       b+=1



# a=[1,2,3]
# print(a*2)

# lst=[10,20,30]      ##Target 10,20, 20,30, 10,30
# for i in lst:
#     for j in lst:
#         if i!=j:
#             print(i,j)

# arr=[1,2,4,5,7]
# for i in arr:
#     for j in arr:
#         if i+j==9:
#             print(i,j)
#
# a=[2,3,4,3,2]
# for i in a:
#     for j in range(i):
#         if i==j:
#             print(i,j)

# x=[10,20,30,40]
# # for i in range(len(x)):
# #     print(i)
# #     print(x[i])
#
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         print(x[i],x[j])

# a=['a','b','c']
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         print(a[i],a[j])

# x=['a','b','c','d','e']
# for n in range(len(x)):
#     for k in range(n+1,len(x)):
#         print(x[n],x[k])

# a=[5,2,3,4,3,2,1,5]
# for x in range(len(a)):
#     for y in range(x+1, len(a)):
#         if a[x]==a[y]:
#             print(a[y])


# b=[1,2,3]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             print(a[i])
# for x in a:
#     for y in b:
#         if x==y:
#             print(y)

# a=[10,20,30,40]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if i!=j:
#             print(a[i], a[j])


# a=['a','b','c','d']
# for i in range(len(a)):
#1     for j in range(i+1,len(a)):
#         if a[i]!=a[j]:
#             print(a[i],a[j])

# a=[2,3,4,3,2]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(a[j])


# a=[1,2,4,5,3,6,7]   for i in a:  for j in range(i):  if i+j==9:  print(i,j)

# a=[1,2,4,5,3,6,7]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==9:
#             print(a[i],a[j])

# a=[2,3,4,3,2]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==a[j]:
#             print(a[i])

# a=[1,2,4,5,7]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==9:
#             print(a[i],a[j])

# a=[1,2,3,4,5,6,7,8,9]
# b=[2,4,6,8]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             print(a[i])
# for i in a:
#     for j in b:
#         if i==j:
#             print(j)

# a=[2,3]
# for i in a:
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")

# a=list(input("enter the word: "))
# b=list(input("Enter the second word: "))
# a.sort()
# b.sort()
# if a==b:
#     print("anadrom")

# a=["eat","ate","ten","tea"]
# for i in range(len(a)):
#     b=list(a[i])
#     b.sort()
#     for j in range(i+1, len(b)):
#         if b[i]==b[j]:
#             print(b[i])

# a=[88,77,55,33,56,45,56]
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         if a[i]>a[j]:
#             print(a[i])

# n=[100000,150000,200000,250000,300000,350000,400000]
# for a in range(len(n)):
#     for b in range(len(n)):
#         if n[a]>n[b]:
#             print('')
#
#             print(n[a])
#             # for c in range(len(n)):
#             print(n[a])

# a=[1,2,3]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         for k in range(j+1, len(a)):
#             if a[i]!=a[j] and a[j]!=a[k]:
#                 print(a[i],a[j],a[k])

#
# colors=["red","blue"]
# size=["S","M"]
# for i in range(len(colors)):
#     for j in range(len(size)):
#         print(colors[i], size[j])
#     print()
#
# for i in colors:
#     for j in size:
#         print(i,j)

# a=[10,20,30,40,20,10]
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]==a[j]:
#             print(a[i])
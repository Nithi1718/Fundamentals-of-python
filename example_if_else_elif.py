# ## Multiples of both 3 and 7
# a=int(input("Enter the number: "))
# if a%3==0 and a%7==0:
#     print("The number is divisible by 3 and 7")
# else:
#     print("This is not a number")

# a=input("Enter the username: ")
# if len(a)>=4 and len(a)<=8:
#     print("valid username")
# else:
#     print("unvalid condition")

# temp=int(input("Enter the temperature: "))
# if temp<=32:
#     print("Cold")
# elif temp<=65:
#     print("hot")
# elif temp<=85:
#     print("very hot")
# else:
#     print("not registered")

## checking the empty list
# a=[1,2,3,4,5]
# print(a)
# b=int(input('Enter the numbere: '))
# if b in a:
#     print("Satisfied")
# else:
#     print("number is not in list")

# a=input("enter the word: ")
# b=input("enter the word: ")
# if a==b:
#     print("equal")
# else:
#     print("not equal")

# a=list(input("enter the word: "))
# b=a.copy()
# b.reverse()
# if a==b:
#     print("palindrome")
# else:
#     print("not palindrome")

# day=input("Enter a day: ")
# if day=="mon" or day=="tue" or day=="wed" or day=="thu" or day=="fri":
#     print("Weekdays")
# elif day=="sat" or day=="sun":
#     print("Week ends")
# else:
#     print("not a valid day")

# a=int(input("Enter the number: "))
# if a>=13 and a<=19:
#     print("Teenager")
# else:
#     print("not a teenager")

# a=int(input("Enter the year: "))
# if a>=2000 and a<=2100:
#     print("21st Century")
# else:
#     print("not 21 Century")

# a=input("Enter a number:  ")
# b=int(a)
# if a!=str:
#     print("only numbers")
# else:
#     print("contains other than numbers")

# a=int(input("enter the number: "))
# # print(b)
# for i in range(1,a):
#     if i*i==a:
#          print("perfect square",i)


    # elif i*i!=a:
    #     print("not perfect square")


# else:
#     print("not square")

# for i in (1,2,3,4,5,6,7,8):
#     for j in range(i):
#         if  i+j==9:
#             print(i,j)


# for i in range(1,10):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(1,10):
#     for j in range(i):    ## the range is between (1,1) so its start with 1 and end before 1...
#                             ### Loop runs from the second time
#         print(i,end='')
#     print()

##Check anagram
# a=(input("Enter the word: "))       ## we can also use list condition to check anagram
# b=(input("Enter another word: "))
# # a.sort()
# # b.sort()
# if sorted(a)==sorted(b):
#     print("Anagram")
# else:
#     print("not a anagram")


### palindrome
# a=list(input("Enter the word: "))
# b=a.copy()
# b.reverse()
# if a==b:
#     print("palindrome")
# else:
#     print("Not")

# a=input("palindrome checking: ")
# if a==a[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

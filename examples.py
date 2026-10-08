# ## positive or negative
# a=int(input("Enter a number to check positive or negative: "))
# if a>0:
#     print(a, "is even")
# elif a==0:
#     print("Error, for applying zero")
# else a<0:
#     print(a," is negative")

# ## Check whether odd or even
# a=int(input("Enter a number: "))
# if a%2==0:
#     print("Even")
# elif a%2==1:   ##else: (simply else used here)
#     print("odd")

# ## Leap year checking
# a=int(input("Enter the year in numbers: "))
# if a>0 and a%4==0:
#     print("Leap year")
# else:
#     print("The given year is not a leap year")

# ## Elder or child
# a=int(input("Enter the number: "))
# if (a>=18):
#     print(f"He is an adult")
# else:
#     print("you are an child")

# ##Check an vowel
# a=input("Enter an alphabet: ")
# if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
#     print(a,", is an vowel")
# else:
#     print("Its not an vowel")

# ## String is empty
# g=input("Enter anything in string format: ")
# if g!="":
#     print("The string is not empty")
# else:
#     print("The  string is empty")

## Divisiblity by 5
# a=int(input('Enter a number: '))
# if a%5==0:
#     print(a, "is divisible by 5")
# else:
#     print("its not divsible by 5")

## Check the letters start with "A"
# a=input("Enter a word: ")
# if a[0]=="a" or a[0]=="A":
#     print(a, ", starts with a or A")
# else:
#     print("The word starts with some other character")

# ##wether the number is between the range
# a=int(input("Enter the number between 10 to 20: "))
# if a>=10 and a<=20:
#     print(a)
# else:
#     print("Enter the number ebetweeen 10 and 20")

# ##Check the list contain the specific element
# lst=["name","age","weight","height","city"]
# a=input('Enter  "name, age, height, weight, city": ')
# if a in lst:
#     print(a,"is in the list")
# else:
#     print("The word is not present in the list")

# ##check both numbers are equal
# a=int(input("Enter the 1st number: "))
# b=int(input("Enter the 2nd number: "))
# if a==b:
#     print("Both numbers are equal")
# else:
#     print("There are not equal")

# ## My own Example to check the specific character in the list
# a=input("Enter a word: ")
# b=input("Enter the letter to check in the word: ")
#
# if b in list(a):
#     print(b,"is present in",a)
# else:
#     print("The given letter is not present in the word")

# ##check whether a number is zero or positive or negative
# a=int(input("Enter a number: "))
# if a<0:
#     print("The number is negative")
# elif a>0:
#     print("The number is positive")
# else:
#     print("The number is zero")

# ##check the length of the password
# a=input("Enter the password: ")
# if len(a)<8 or len(a)>8:
#     print("The password does not has exactly 8 characters")
# else:
#     print("The character length matched")

# ##check for palindrome
# a=list(input("Enter a word: "))
# b=a.copy()
# b.reverse()
# if a==b:
#     print(a, "The word is palindrome")
#
# else:
#     print("Not a palindrome")

# ##voting eligiblity
# a=int(input("Enter your age: "))
# if a>=18:
#     if a >=75:
#         print("You are the senior citizen")
#     else:
#         print("You are eligible")
# else:
#     print("you are not eligible to vote")

# ## Elif condition
# a=int(input("Enter the marks: "))
# if a<30:
#     print("You are fail")
# elif a<60:
#     print("average")
# elif a<=80:
#     print("Good")
# else:
#     print("pass")

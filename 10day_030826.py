## Function definition__(Body)__(function calling)__(instance)
## 2 Function (Pre-defined functions, User-defined functions)
## Argument passing has 4-5 types (Positional, Variable, Default, Anamous, KWargs)


#### Simple addition using functions

# def add(a,b):  ## Functions definition
#     print(a+c)           ## Body
# add(2,3)                            ## Function calling using function name
# add(4,5)


#### Finding odd or even using functions

# def square(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("odd")
# square(4)
# square(8)
# square(12)
# square(35)


#### Printing 2 table

# def table_2(a,b):
#     for i in range(a,b):
#         print(f"{2}X{i}={2*i}")
# table_2(1,6)
# table_2(6,11)
# table_2(11,16)
# table_2(16,21)


# ### Printing Reverse from 10 - 1
#
# def reverse_num(a,b):
#     for i in range(a,b-1,-1):
#         print(i)
#
# reverse_num(10,1)
# reverse_num(20,11)


# ### printing numbers from 1 to 10
#
# def numbers(a,b):
#     while a<=b:
#         print(a)
#         a+=1
# numbers(1,11)

# ### printing star pattern
#
# def star(a,b):
#     for i in range(a,b+1):
#         print(" "*(b-i)+"*"*((2*i)-1))
# star(1,5)


### Argument Passing(Types)

# ## Positional
# def add(a,b):
#     print(a+b)      ## We pass argument using position and the position is already given
# add(1,2)

# ## Variable
# def add(a,b):
#     print(a+b)
# add(b=3,a=4)
# add(4,5)
# add(a=5,b=8)
# add(b=7,a=10)

# ## Default
# def sub(a,b=1):        ## Here default b value is 1. but we can change when we need
#     print(a-b)
# sub(1)
# sub(5)
# sub(5,9)        ## Here, i assign new value 9 to the variable (b).. But this is temporary
# sub(19)     ## here we again have the default value of b as 1(one)


# ## Anamous (*a)
# def add_multiple(*a):     ##  Pass Multiple values at the one so we use(*a)
#     print(sum(a))         ## -sum- is the pre-defined function. -sum- defaultly add all the values in 'a'
# add_multiple(2,5,6,8,4)
# add_multiple(4,6,7)
# add_multiple(5,6,7,1)

# a=[1,2,3,4]           ## my own example for pre_defined function --sum--
# print(sum(a))

# ## KWarsgs (**a)
# def diction(**a):       ## Gives the output in --key:value pair--
#     print(a)
# diction(a=1,b=1,c=4,n=9)


# ## passing all the arguments in line code
# def all(a,b,*c,d=7,**e):      ## i am using all type of argument here
#     print(a+b+d,"\t\t\t",sum(c),"\t\t",e)
# all(1,2,3,4,5,x=9,y=7,z=10)
# all(3,5,5,6,7,7,8,8,9,age=23,name="nithi")


### Examples using Function
## Position argument passing

# def define(name,age, height):
#     print(f"my name is {name} and i am {age} years old... i am {height} height tall")
#     print()

# define("nithish",23,168)
# define("vembu",23,161)
# define("vino",23,160)


# ## Variable argument passing
# def main(a,b):
#     print(a+b)
#
# main(b=5,a=5)
# main(b="nithi",a="143")
# main(a=17,b=18)


# ### Default argument passing
# def logo(a,c,b=7):
#     print(a+c-b)
# logo(8,9)
# logo(a=1,b=5,c=9)
# logo(4,5,3)

# ### Anamous argument and Kwarg argumnt passing at the same time using for loop:
# def logo(a,*cos,**sin):
#     while a<(sum(cos)):
#         print(sin)
#         a+=1
# logo(1,2,3,x=7,y="nithi")
# logo(2,2,2,x=1,y=9,z=10)

# ### Anamous argument passing
#
# def logo(*n):
#     print(n)
# logo(1,2,235,4564)
# logo(1,3,5,6,8)
# logo("nithi","","kumar",'s')

# ## Anamous argument passing and using the predefined function --sum--
# def logo(*n):
#     print(sum(n))
# logo(1,23,45,6)
# logo(2.3,53,3,3,34,34,3.7,7)


# ### KWargs argument passing (((Always gives the output in Key Value pair)))
# def logo(**d):
#     print(d)
# logo(x=2,v=4)
# logo(x=3,v=4,z=6,y=5)
# logo(x=4,v=6,y=8)


# ### All type of argument passing in single statement
#
# def logo(a,*c,b=1,**d):
#     print(a+b,sum(c),d)
#
# logo(5,2,3,4,6,x=0,y=19,z="name",f="age")
# logo(8,44,4,5,5,44,4,name="nothing",age=20,height=168)


# def dragon(a,b):
#     for i in range(1,a+1):
#         print(" "*(5-i),"*"*(2*i-1))
# dragon(5,5)
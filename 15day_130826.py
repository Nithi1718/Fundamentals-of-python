# try:
#     class University:
#         def __init__(self, name, year, NAAC):
#             self.name=name
#             self.year=year
#             self.NAAC=NAAC
#
#         def show_info(self):
#             print(self.name, self.year, self.NAAC)
#
#         def show_uni(self, uni_name):
#             print(f"The name of the university is {uni_name}")
#
#     class Course(University):
#         def show_course(self, course_name):
#             print(f"The name of the course is {course_name}")
#
#     class Branch(University):
#         def show_branch(self, branch_name):
#             print(f"The name of the course is {branch_name}")
#
#     class Student(Course, Branch):
#         def show_student(self, student_name):
#             print(f"The name of the course is {student_name}")
#
#     class Faculty(Branch):
#         def show_faculty(self, faculty_name):
#             print(f"The name of the faculty is {faculty_name}")
#
# except Exception as a:
#     print(a)
#
#
# s1=Student("isha",2007,"A++")
# s1.show_info()
# s1.show_student("Nithish Kumar")


# a=open(r"C:\Users\NITHISH KUMAR\OneDrive\Desktop\nnn.txt",'w+')
# print(a.readlines(30))
# print(a.readline())
# a.writelines("helo i am an ai ml engineer")
# a.flush()
# a.write("\nnothing to worry take care")
# a.flush()
# a.writelines("\nHelo i am Nithish\nI am studying in Fita Academy\nI am currently in study hall")
# print(a.tell())
# print(a.seek(120))
# print(a.tell())

# print(a.read())
# a.write("hey bro this is easy")
# print(a.read())
# a.close()
# print(a.read())





# class Grandpa:
#     def gsource(self):
#         print("I gave them energy to learn and earn in their life")
#
# class Father(Grandpa):
#     def fsource(self):
#         print("i have own 5bhk house in chennai")
# class Mother(Father):
#     def msource(self):
#         print("i have 2 cars and 8 crore bank balance")
#
# class Child(Mother, Father):
#     def csource(self):
#         print("I am working as the AI & ML engineer in Microsoft, Singapore and USA")
#
# nithish=Child()
# nithish.csource()
# nithish.fsource()
# nithish.gsource()
#
# nithya=Mother()
# nithya.msource()
# nithya.gsource()

# class Father:
#     def men(self,king, maker):
#         print("first one")
#
#     def gen(self):
#         print("second one")
#
#     def hen(self):
#         print("third one")


# nun=Father()
# nun.men("Yes","No")
# nun.gen()
# nun.hen()

# print(round(12.5)-round(11.5))

# a=["n","m","b",'d']

# for index,i in enumerate(a,start=1):
#     print(index,i)

# b=0
# for i in a:
#    b+=1
#    print(b,i)

class Step:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def men(self):
        print(f"{self.name}\n{self.age}")
s=Step("Nithish",23)
s.men()
print(s.name)
print(s.age)

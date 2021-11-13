
# Lamda or annonmus functions

# minus = lambda x,y: x-y
#
# def minus(x,y):
#     return x-y
# print(minus(3,5))

# def a_first (a):
#     return a[1]

# a =[[8,1],[2,3],[4,5]]
# a.sort(key=lambda x:x[1])
# print(a)


# Health Management System
# 3 clients - Harry, Rohan and Hammad
# H_DietLog, H_exerciseLog, R_DietLog, R_ExerciseLog
# Ha_DietLog, Ha_ExerciseLog

#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# def append(client):
#     d = int(input("Choose Log type\n1 for 'Diet'\n2 for 'Exercise'"))
#     if d == 1:
#         with open(client + "diet.txt", "a") as file:
#             en = input("enter your Diet\n")
#             file.write("["+str(getdate())+"]: "+en+"\n")
#     elif d == 2:
#         with open(client + "ex.txt", "a") as file:
#             en = input("enter your Exercise\n")
#             file.write("["+str(getdate())+"]: "+en+"\n")
#
#
# def read(client):
#     d = int(input("What you want to retrieve\n1 for 'Diet'\n2 for 'Exercise'"))
#     if d == 1:
#         with open(client + "diet.txt") as file:
#             p = file.read()
#             print(p)
#     elif d == 2:
#         with open(client + "ex.txt") as file:
#             p = file.read()
#             print(p)
#     return p
#
#
# print("Health Management System")
# inp = int(input("Choose your client"
#                 "\n1 for 'Harry'"
#                 "\n2 for 'Rohan'"
#                 "\n3 for 'Hammad'"
#                 ))
# cl2 = int(input("1 for 'Log'\n2 for 'Read'"))
# Client = ''
# if inp == 1:
#     Client = "Harry"
# elif inp == 2:
#     Client = "Rohan"
# elif inp == 3:
#     Client = "Hammad"
# if cl2 == 1:
#     append(Client)
# elif cl2 == 2:
#     read(Client)
# random_Bname = random.randint(4,5,)
# print(random_Bname)


# import random
# list_of_Baby_name = ["Ilyas","Atta Muhammad","Ali"]
# choice = random.choice(list_of_Baby_name)
# print(choice)

# import namegenerator
# def read(namegenerator):
#     d = int(input("Choose Log type\n1 for 'Diet'\n2 for 'Exercise'"))
#
# print (namegenerator.gen())


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 02:55:41 2019

@author: Garrett Sloup

GIRL NAME GENERATOR
POSSIBLE GIRL NAMES WITH A MIDDLE CHARACTER OF "D"

Program reads a txt file (girlNamesList.txt) of the 1000 most common baby girl names from:
    https://www.verywellfamily.com/top-1000-baby-girl-names-2757832

Program also has access to 2287 other girl names (longerGirlsNameList.txt).
    Link can no longer be found.


Will go through each name and determine if the name has an odd num of
characters and the middle character is a "d".

v2)Adds functionality to take the returned list of possible names and will
# names = ["Maddy", "Sadie", "Addison", "Jade"]
#
#
# def exampleLogic(names):
#     """
#     Iterates through a list of names, printing out whether or not
#     a particular name is both an odd num of letters and the
#     middle char is a 'd'.
#
#     returns NoneType
#     """
#     for name in names:
#         # checks if num letters in name is odd
#         if len(name) % 2 == 1:
#             # checks if the middle letter is a 'd'
#             if name[len(name) // 2] == "d":
#                 print(name + " is a possiblity")
#             else:
#                 print(name + "'s middle letter isn't a 'D'.")
#         else:
#             print(name + "'s name has even letters.")
#     eliminate any duplicate names.
# """
# #


# Tests logic used to determine valid name
# UNCOMMENT LINE BELOW TO RUN
# exampleLogic(names)


# Word file containing top 1000 girls' names
# WORDFILE = "girlNamesList.txt"


# me = "Harry"
# a = "THis  is %s"%me
# print(a)

# import math
# me = "Ilyas"
# a1 = 34
# # a = "This is %s %s"%(me. a1)
# a = f"This is {me} {a1} {math.tan(45)}"
# print(a)

#        Water Gun Game #
#
# import random
# inp = int(input("Choose your choice:\n1:Snake\n2:water\n3:Gun:\n"))
#
# while(inp<10):
#     if (inp == 1):
#         list_inged = ["Snake", "water", "gun"]
#         choice = random.choice(list_inged)
#         if (choice == "water"):
#             print("The computers choice",choice)
#             print("You Won! Congrats")
#         else:
#             print("The computers choice",choice)
#             print("You Loss! Opps")
#     if (inp == 2):
#         list_inged = ["Snake", "water", "gun"]
#         choice = random.choice(list_inged)
#         if (choice == "gun"):
#             print("The Computer choice is", choice)
#             print("You Won! Congrats")
#         else:
#             print("The Computer choice is", choice)
#             print("You Loss! Opps")
#     if (inp == 3):
#         list_inged = ["Snake", "water", "gun"]
#         choice = random.choice(list_inged)
#         if (choice == "gun",):
#             print("The Computer choice is", choice)
#             print("You Loss! Opps")
#         else:
#             print("The Computer choice is", choice)
#             print("You Won! Congrats")
#
#     break
#

 # **************************Learning normal ,*args **kwargs

# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
# function_name_print("ilyas","Ismail","umar","Ali","idrees")

# def funarg(normal,*args,**kwargid):
#     for items in args:
#         print(items)
#     for key,value in kwargid.items():
#         print(f"{key} is a {value}")
# ily = ["ilyas","Ismail","umar",
#        "Ali","idrees","Atta","This my program"]
# normal = "This is a normal arguments",\
#          "This is an abnormal arguments"
# kw = {"ilyas":"programmer","Ali":"Teacher","idrees":"student","umar":"Hafiz"}
# funarg(normal,*ily,**kw)


# l1 = ["Bhindi","Aloo","Sabzi","Matr"]
#
# # for item in l1:
# #     i = 1
# #     if i%2 is not 0:
# #         print(f"ilyas bring the {item}")
# #     i += 1
#
# for index, item in enumerate(l1):
#     if index%2==0:
#         print(f"ilyas bring the {item}")


# ********************Learning Time module in python***********

# import time
#
# intial = time.time()        # Time function gives number of ticks in time module and one tick is one second
#
# k = 0
# # while (k<35):
# #     print("While loop ran in :",time.time()-intial)
# #     print("This is idrees bahi")
# #     time.sleep(2)
# #     k+=1
# for i in range(35):
#     print("For loop ran in :", time.time() - intial)
#     print("This is Muhammad ilyas")
#
#
# #**************** Way to calculate local time****************
#
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# ******Importing functions and using "__main__" **********

# def printily(string):
#     return f"Ye Code Ilyas ko pakkra do Thakaur{string}"
#
# def add(num1, num2):
#     return num1 + num2
#
# print("The value of ",__name__)
# if __name__ == '__main__':
#     print(printily("Ilyas1"))
#     o = add(4, 5)
#     print(o)

# **** Learning about Join  Functions in python*******************
# lis1 = ["Joan","Cena","shivium","Kali",
#         "Kavin Ovien","Brok Laisner"]
#
# # for items in lis1:
# #     print(items," and" ,end=" ")
#
#
# a = " and ".join(lis1)
# print(a)
# print("Other WWE Super Satrs of WWE")


# *******************Map Filters and reduce  in python***********
# numb = ["3","4","5"]
# numn = list(map(int, numb))
# numb[2]= numb[2] + 1
# num = [2,3,4,5,6,6,]

# num = [2,3,4,5,6,8]
# sq =  list(map(lambda x:x*x ,num))
# print(sq)

#
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# fun = [square ,cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i), fun))
# print(val)


# ********** practice Codes only for map functions
# print(numbers[2])
# print(map(int,numbers))
# for i in range(len(numbers)):
#     numbers [i] = int(numbers[i])

# ************************Filter Functions in Pythons*******************
#
# list1 = [1,2,3,4,6,7,9]
#
# def is_grater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_grater_5,list1))
# print(gr_than_5)

# ***********************REDUCE*****************************

# Practice works for Reduce functions in pythons
# num = 0
# for i in lis:
#     num = num + i
# print(num)

#*Real work for Reduce functions in python
# from functools import reduce
# lis = [1,2,3,4,5]
# num = reduce(lambda x,y:x*y,lis)
# print(num)

# *********************Decoritive Functions***************
# Practice work for Decorative
# def function1():
#     print("Subscribe Now")
#
# func = function1
# func()
# del function1

# def funcert(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a = funcert(0)
# print(a)
#
# def executors(func):
#     func("this")
#
# executors(print)

# def dec1(func1):
#     def nowexe():
#         print("Executing Now")
#         func1()
#         print("Executed")
#     return nowexe()
# # @dec1
# def who_is_harry():
#     print("Harry is a good boy")
# who_is_harry = dec1(who_is_harry)
# who_is_harry()


# ****************OPPS in Python*************************
# class students:
#     pass
# idrees = students()
# ilyas = students()
#
# idrees.name = "Edoo"
# ilyas.cla= 12
# idrees.section = "none"
# ilyas.salary = 30000000000
#
# print(idrees.section)

# ******************Self and init Constuctor in python***************
# class students:
#     no_of_leaveas = 8
#
#     def __init__(self, aname, asalary, arole ):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"
# idrees = students("Muhammad idrees",459390,"instructors")
# # ilyas = students()
# #
# # idrees.name = "Edoo"
# # idrees.role = "doctor"
# # idrees.salary = 40000000000000
# # # ilyas.cla= 12
# # # idrees.section = "none"
# # ilyas.name = "hilly"
# # ilyas.role = "Learner"
# # ilyas.salary = 30000000000
# print(idrees.salary)

# *****************************Class Method in python***************************************
# class students:
#     no_of_leaveas = 8
#
#     def __init__(self, aname, asalary, arole ):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#      return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"
# #
#     @classmethod
#     def change_in_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     def __init__(self, aname, asalary, arole ):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"
#
# idrees = students("Muhammad idrees",459390,"instructors")
# students.no_of_leaveas = 100322
# print(idrees.no_of_leaveas)
#

# ***********************class methods as an alternative consturctor***************************
# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     @classmethod
#     def from_dash(cls, string):
#         # params = string.split("-")
#         # print(params)
#         # return cls(params[0], params[1], params[2])
#         return cls(*string.split("-"))


# harry = Employee("Harry", 255, "Instructor")
# rohan = Employee("Rohan", 455, "Student")
# karan = Employee.from_dash("Karan-480-Student")
#
# print(karan.no_of_leaves)
# rohan.change_leaves(34)
# print(harry.no_of_leaves)

# **************************** Pythons in one Video*********************

# a = '''Ilyas
# is
# a Good boy'''
# a = 'Ilyas' #Methods to write strings
# a = "Ilyas"
# b = 35
# c = 5>3
# d = None
# Printing the types of variables
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# *****************************Arthimatic Opreators*************************************
# print("The value of 3-4 is:",3-4)
# print("The value of 3+4 is:",3+4)
# print("The value of 3*4 is:",3*4)
# print("The value of 3/4 is:",3/4)

# ***************************Assaign Operator*************************************************
# a = 2
# # a += 3
# # a -= 3
# # a *= 3
# a /= 3
# print("The value of :",a)

# ***************************Comparison Operator*************************************************
# a = True
# b = False
#
# print("The value of  a and b ", a and b)
# print("The value of  a and b ", a or b)
# print("The value of  not b ", not b)

# ***************************Typecasting*************************************************
# a = "3984"
# a = int(a)
# print(type(a))
# print(a + 5)

# ***************************Input Function*************************************************
# a = input("Enter Your Number:")
# print(a)
# print(type(a))
# a = int(a)   #converting 'a' into integer
# print(a)
# print(type(a))

# *************************************String***************************************
# a = 'ilyas"'
# a = "ilyas's" # use this if you have single quote in your code
# a = '''ilyas's and ilyas"''' # Use this if you uses the single and double quote
#                             # your comment
# b = 56
# print("The Name is Muhammad ",a ,"\nThe value is of a number is:",b)
# print(type(a))

# *************************************String Slicing***************************************
# a = "Asslamo Alakum "
# b = "Kase ho ilyas"
# sum = a+b # This is the method in which we can concatenating the two strings
# print(type(a))
# print(sum)
# print(type(b))
#
# b = "Kase ho ilyas"
# print(b[1:5])
# b[3] = 'b'
# We cannot chage any string character value
# print(len(b))
# print(b[-1])

#    We can skip the any character of string by using only end slicing [1:2:3]
# print(b[1::2])

# *********Lists[] in Python************************
# a = [1,3,44,5,77,8]
# print(a)
# print(a[4])
#
# # Replacing the index[1] value of 3 in the list with 100
# a[1] = 100
# print(a)

# This method is also valid that we can put multiple datatypes in a list i.e
# lis2 = [354,False, 45.4, "Ilyas"]
# print(lis2)

# *****************List Slicing**********************
# friends = ["Harry","Idrees","Rohan","Sam","Umar",34]
# print(friends[0:5])

# *****************List sorting**********************
# l1 = [12,152,119,13,576,49,93]
# l1.reverse()
# l1.remove()
# l1.append(33) # Adds 33 at the end of the list
# l1.sort()
# l1.insert(1, 566) #insert 544 at index 2
# l1.remove(12)
# l1.pop()
# print(l1)

# ****************************Touple*****************************

# # t = (1,)
# t = (1,2,44,5,6,7,989,1,1,1,1,5)
# print(t.count(5))

# *************************Dictionary***************************
# MyDict = {
#     "Fast":"In a quick Manner",
#     "Harry":"Is a  good Teacher",
#     "Mango":"Is a sweet fruit",
#     "anotherDict": {'harry':'Player'}
# }
# print(MyDict["Fast"])
# MyDict['Fast'] = [1,3,5,6] # Is Muatable
# print(MyDict["Harry"])
# print(MyDict["anotherDict"]["harry"])
# print(MyDict["Fast"])



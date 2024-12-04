#condition types 
# if isinstance(value, dict):
# print("dict")
# elif isinstance(value, list):
# print("list")
# elif isinstance(value, tuple):
#   print("tuple")
# end condition types

#1) if
#2)if else
#3) if ...elif ...else
# age = 20
# if age >= 18:
# print("you are eligible to vote")
# else:
# print("you are not eligible to vote")
# 
# 
# merge = 25
# if merge > 18:
# print("you are merge")
# print("you are eligible to vote")
# print("you are eating")
# 
# 
#class work 
# WAP to output like child ,adult old
#  
# age  = 38
# if age > 12:
# print("child")
# elif age > 38:
# print("adult")
# else:
# print("old")
# 
# 
# age = 60
# if age > 12:
# print("child")
# if age > 38:
# print("adult")
# else:
# print("old")
# 

from re import A


age = "e"
#if age.isdigit() == False:  # if not age.isdigit():
if isinstance(age,str) and age.isdigit() == False:  # if not age.isdigit():
    print("invalid input")
elif age>0 and age<12:
    print("child")
elif age>12 and age<18:
    print("teen")
elif age>18 and age<60:
    print("adult")
else:
    print("old")
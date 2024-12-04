# input("string") -> str
# input("number") -> int
# input("float") -> float
# input("list") -> list
# input("tuple") -> tuple
# input("dict") -> dict
# input("bool") -> bool



#age = input("Enter your age?#>>>")
#print("your age is",age)



age = input("Enter your age?#>>>")
age = int(age)
#if age.isdigit() == False:  # if not age.isdigit():
if isinstance(age,str) and age.isdigit() == False:  # if not age.isdigit():
    print("invalid input")
elif age>0 and age<12:
    print("child")
elif age>12 and age<18:
    print("teen")
elif age>18 or age<60:
    print("adult")
else:
    print("old")
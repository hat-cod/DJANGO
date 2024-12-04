data = ("   name is roshan    ")
print(data.strip())# Output: name is roshan
print(data.rstrip())# Output:   name is roshan
print(data.lstrip())# Output: name is roshan
#print(data.split(,))# Output: ['name', 'is', 'roshan']




data = ("   name is roshan    ")

print(data.upper())# Output: NAME IS ROSHAN  upper function is all letter in 
print(data.lower())# Output: name is roshan
print(data.capitalize())# Output: Name is roshan
print(data.title())# Output: Name Is Roshan
print(data.swapcase())# Output: NAME IS ROSHAN
print(data.replace("name", "ram"))# Output: ram is roshan
print(data.replace("name", "ram", 1))# Output: ram is roshan
print(data.replace("name", "ram", 2))# Output: ram is roshan
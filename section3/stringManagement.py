# String

myFavoriteGroup = "Foals"
comentary = "The best band"

# String concatenation in Python

# Simple way. Only valid with string data.

print("My favorite music group is: " + myFavoriteGroup + " " + comentary)

# If used with number types, + operand acts as a sum

# Using strings

num1 = "1"
num2 = "2"
print(num1+num2)

# int() converts a string to a number. But the string should be a number in numerical form, i.e. 90.

print(int(num1) + int(num2))

# Concatenation using print function syntaxis, separating arguments with a comma, when printing, a space is added between
# arguments. 

print("My favorite music group is:", myFavoriteGroup, comentary)

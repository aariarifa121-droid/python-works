# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math
try:

    num = int(input("enter a number:"))

    print("factorial",math.factorial(num))

except ValueError:
    print("invalid")    

    
# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist




#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

d = {"name": "arun","age": 23,"place": "ekm"}

try:
    key = input("Enter a key: ")
    print("Value:", d[key])

except KeyError:
    print("Key does not exist.")
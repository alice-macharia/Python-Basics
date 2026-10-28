# if else
import os

name = input("what is your name?:")

age = input("Enter the age:")

if not age.isnumeric():
    print("Invalid age")
    #terminate
    os._exit(0)

if int(age) > 18:
    print( name+"is an adult")
else:
    print(name+"is a child")

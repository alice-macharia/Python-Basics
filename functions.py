#functions methods
print("Hello World") #built in

with open("temp.text", "w") as file:
    file.write("99.34\n")
    file.write("100\n")
    file.write("100\n")

with open("temp.text", "r") as file:
    content=file.read()
    print(content)
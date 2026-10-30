#oop
#object --> laptop ->
#name --> props
#classes

class Person:
    #constructor
    def __init__(self, name, age, dob, weight, height, color):
        self.name = name
        self.age = age
        self.dob = dob
        self.weight = weight
        self.height = height
        self.color = color

    def display(self):
        print(self.name)
        print(self.age)


    def get_bmi(self):
        result = self.weight/ = self.height ** 2
        return  round(result,2)


#blueprint for creating objects

#invoking the constructor
p1= Person("Duke Dennis", 20, "8-9-2007", 65.7, 1.6, "Black")
p1.display()
p2= Person("Harry Harris", 30, "9-10-2009", 100, 2.7, "White")
p2.display()
p2.display()


print(f"{p1.name} {p1.get_bmi()}")
print(f"{p2.name} {p2.get_bmi()}")
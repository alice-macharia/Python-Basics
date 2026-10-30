#oop2
class Circle:
    def __init__(self, r):#setup
        self.radius = r

    def area(self):
        return 22/7 * self.radius**2

    def perimeter(self):
        return 22/7 * self.radius*2

    def print_details(self):
        print("Radius is", self.radius)
        print("Perimeter", self.perimeter())
        print("Area is", self.area())

c1= Circle(10)
c2= Circle(54)
c3= Circle(7)

print(c1.area())
c1.print_details()
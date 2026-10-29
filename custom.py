def greet():
    print("Hello")


def greeting(name):
    print(f"Hello  {name}")


def volume_cylinder(radius, height):
    v = 22 / 7 * radius ** 2 * height
    print(round(v, 2))


def volume_cylinder_better(radius, height):
    v = 22 / 7 * radius ** 2 * height
    return v


def volume_surface(radius, height):
    v = 22 / 7 * radius ** 2 * height
    c = 22 / 7 * radius ** 2 * height + 22 / 7 * radius * 2 * height
    return v, c


# greet() #call== use no arguments
greeting("John")
greeting("Michael")
greeting("James")

volume_cylinder(10, 20)
volume_cylinder(15, 25)
volume_cylinder(12, 24)

result= volume_cylinder_better(10, 8.9)
print(result)

with open("volumes.txt", "r") as file:
    file.write(str(result))

volume, area = volume_surface(10, 30)
print(volume)
print(area)

#named parameters
v, a = volume_surface(height=10, radius=5)
print(v)
print(a)


def divide(d, b, should_round=False):
    res= d/ b
    if should_round:
        return round(res, 2)
    else:
        return res

print(divide(454, 7788, True))
print(divide(4, 10, False))

print(divide(4, 10, True))
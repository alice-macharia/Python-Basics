def add(a, b):
    res = a + b
    return res


def addition(*nums):
    """
    Returns sum of nums
    Parameters:
        integers or floats or a mixture of integers and floats
    Returns:
        sum of integers or floats
    """

    total = sum(nums)
    return total


def build_profile(**kwargs):  #dict key-word agrs
    for k, w in kwargs.items():
        print(k, w)


def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)


addition(8, 8, 9, 8)

#anonymous ==lamda
# def square(num):
#     return num * num
#
# result=square(3)
# print(result)


#{"name": "Jerry" "age":18}

# build_profile(experience="100", name="Jane")

#call function
# print(add(9,10 ))
# print(addition(1,2,3,4,5))

square = lambda num: num * num

print(square(5))
res = square(2.9)
print(res)

surface_area_cylinder = lambda r, h: 22 / 7 * r ** 2 * 2 + 22 / 7 * 2 * r * h

print(surface_area_cylinder(5, 6))

people = [
    {'name': 'John', 'age': 95, 'height': 48},
    {'name': 'Alex', 'age': 45, 'height': 68},
    {'name': 'Bob', 'age': 19, 'height': 80},
    {'name': 'Meshach', 'age': 27, 'height': 79},
]

#lambda x:x['age]
sorted_by_age = sorted(people, key=lambda x: x["age"])
print(sorted_by_age)

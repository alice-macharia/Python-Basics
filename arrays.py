# #store many things
# ages=[21, 30, 49, 90, 50, 60, 52]
#
# names=["Jane, Jack, Moha, Zack"]
#
# #functions
# ages.append(31)
# # ages.clear()
# # ages.sort()
# # ages.reverse()
# print(ages)
#
#
# names.sort()
# print(names)
#
# jack_count = len(names)
# print(jack_count)
#
# print(sum(ages))
# print(sum(ages)/len(ages))
#
# #retrieve an element
# print(ages[0])
# print(ages[5])
# print(ages[-1]) #last element
# print(ages[-3:]) #slicing
# print(ages[:3])

#set
scores = {88, 78, 88, 65, 77, 78}  #no duplicate
print(scores)
scores.add(90)

#tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thu", "Sat", "Sun")
print(weekdays[0])

#dictionary
person={"name": "Jack", "age": 25, "height": 80, "weight": 70}
print(person["name"])
print(person["age"])
print(person["height"])
print(person["weight"])

people=[{"name": "Jack", "age": 25, "height": 80, "weight": 70},
        {"name": "Morris", "age": 25, "height": 80, "weight": 70},
        {"name": "Alice", "age": 25, "height": 80, "weight": 70},
        ]
print(people[0])
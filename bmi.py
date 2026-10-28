# •Underweight: Below 18.5
# • Healthy Weight: 18.5 to 24.9
# • Overweight: 25.0 to 29.9
# • Obesity (Class I): 30.0 to 34.9
# • Obesity (Class II): 35.0 to 39.9
# • Severe Obesity (Class III): 40.0 or higher

weght= input("Please enter your weight: ")
height= input("Please enter your height: ")

w=float(weght)
h=float(height)

bmi= w / h**2

if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi <= 24.9:
    print("You are healthy")
elif 25.0 <= bmi <= 29.9:
    print("You are overweight")
elif 30.0<= bmi <= 34.9:
    print("You are obese class 1")
elif  35<= bmi <= 39.9:
    print("You are obese class 2")
else:
    print("You are obese class 3")



# BMI caculator = (weight)/(height**2)

weight = float(input("enter your weight in killo grams:"))
height = float(input("enter your height in meters:"))
print("BMI=", (weight)/(height**2))

# volume of cylender = 3.14*radious**2 *height

radious = float(input("enter radious of cylender:"))
height = float(input("enter height of cylender:"))
print("volume of cylender=", (3.14*radious*radious*height))

# Area of rectangular = length*width

length = float(input("enter the length of rectangle in centimeter:"))
width = float(input("enter the width of rectangle in centimeters:"))
print("Area of rectangular =", (length*width)) 

# Area of circle = 3.14* radious**2

radious = float(input("radious of circle in centimeters:"))
print("Area of circle =", (3.14* radious**2))

# Area of cube = 6* (edge**2)

Edge = float(input("enter the edge value in cm:"))
print("Area of cube =", 6* (Edge**2))

# Calculate your age = cureent year - birth year

currentyear = int(input("enter current year:")) 
birthyear = int(input("enter your birth year:"))
print("your age =",(currentyear-birthyear))

# convert temperature from
# Celsius to Fahrenheit
first = float(input("enter celcius temperature:"))
print("Fahrenheit temperature=",  (9/5)* first+32)

second = float(input("enter fahrenheit temperature"))
print("Celcius temperature=",(second - 32) * 5/9 )


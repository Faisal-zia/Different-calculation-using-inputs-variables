name = "Faisal-zia"
age = 32

print("my name is : ", name)
print("my age is: ", age)
print(type(name))
print(type(age))
# Arithmatic operator

a = 7
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # divide answer without point value
print(a**b)# power
print(a%b) # remainder

# comparison operator

a = 50
b = 20

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Assignment operator

a = 10

a += 5
print(a)
a -= 5
print(a)
a *= 5
a /= 5
a //= 5

print(a)

# logical operator

# type conversion
#1 type conversion

a = 2
b = 4.25
print(a+b)

#2 type casting

a =int("2") # a = "2" not possible 
b = 4.25

print(a+b)

# inputs  

name = input("enter your name:")
print("welcome", name)

# (results for input always astring)

name = input("enter some value:")
print(type(name), name)

weight = input("enter your weight in killo grams:")
height = input("enter your height in meters:")
BMI = (weight)/(height(**2))
print("BMI")
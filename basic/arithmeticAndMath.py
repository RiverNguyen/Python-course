import math

print(math.pi)
print(math.e)

result = math.sqrt(25)
result1 = math.ceil(5.8)
result2 = math.floor(5.8)
print(result)

# Arithmetic and Math

friends = 5

friends += 1
friends -= 2
friends *= 3
friends /= 4
friends **= 2
friends %= 3

print(friends)

x = 3.14
y = -4
z = 5

result3 = round(x, 1)
result4 = abs(y)
result5 = pow(z, 2)

result6 = max(x, y ,z)
result7 = min(x, y, z)

# Exercise

radius = float(input("Enter the radius of the circle: "))

if radius < 0:
    print("Please enter a positive number")
    exit()

circumference = 2 * math.pi * radius
area = math.pi * math.pow(radius, 2)

print(f"The circumference of the circle is: {round(circumference, 2)}")
print(f"The area of the circle is: {round(area, 2)} cm^2")

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The hypotenuse of the triangle is: {round(c, 2)}")



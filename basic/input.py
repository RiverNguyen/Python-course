# input() function
# input() function is used to take input from the user. It reads a line from the input and returns it as a string.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

age = age + 1

print(f"Hello {name}, you are {age} years old.")

# Exercise 1

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

if length <= 0 or width <= 0:
    print("Invalid input")
    exit()

if length < width:
    length, width = width, length

area = length * width

print(f"The area of the rectangle is: {area} cm²")

# Exercise 2

item = input("What item do you want to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many do you want to buy: "))
total = price * quantity

if price < 0 or quantity < 0:
    print("Invalid input")
    exit()

print(f"The total cost of {quantity} {item} is: ${total}")
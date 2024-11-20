age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
elif age < 0:
    print("Please enter a valid age")
elif age > 100:
    print("Please enter a valid age")
else:
    print("You are not eligible to vote")

# Exercise
res = input("Would you like to continue? (Y/N): ")
if res == "Y":
    print("Continuing ...")
else:
    print("Exiting ...")
    exit()
# Ask the user for two numbers
print("Enter two numbers and I'll sum them up.")
number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
except ValueError:
    print("You can only introduce numbers")
else:
    print(f"Here is the result: {number_1 + number_2}")
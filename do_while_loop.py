# Program to reverse digits using a do-while equivalent
# Author: JBA
# Date: 27-11-2024

# Ask the user for a number
number = int(input("Enter a number: "))

# Reverse digits (Python equivalent to do-while)
print("Reversed number:", end=" ")
while True:
    print(number % 10, end=" ")
    number //= 10
    if number == 0:
        break
print()

# Example Input/Output:
# Enter a number: 12345
# Reversed number: 54321
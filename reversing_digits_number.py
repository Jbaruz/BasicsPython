# Program to reverse the digits of a number
# Author: JB
# Date: 27-11-2024

# Ask the user for a number
number = int(input(" Enter a number: "))

# Reverse the digit
print("Reversed number: ", end=" ")
while number != 0:
    print(number % 10, end=" ")
    number //= 10
print()

# Example Input/Output:
# Enter a number: 12345
# Reversed number: 54321


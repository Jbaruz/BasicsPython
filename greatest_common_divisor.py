# Program to find the greatest common divisor
# Author: JBA
# Date: 27-11-2024

# Ask the user for two numbers
u = int(input("Enter the first non negative integer: "))
v = int(input("Enter the second non negative integer: "))

# use the Euclidean algorithm
while v != 0:
    u, v = v, u % v

# Display the result
print(f"The greatest common divisor is {u}")

# Example Input/Output:
# Enter the first nonnegative integer: 150
# Enter the second nonnegative integer: 5
# The greatest common divisor is 5
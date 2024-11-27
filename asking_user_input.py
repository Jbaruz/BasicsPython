# Program to calculate a triangular number based on user input
# Author: JBA
# Date: 27-11-2024

# Ask the user for input
number = int(input("What triangular number do you want?"))

# Calculate the triangular number
triangular_number = sum(range(1, number + 1))

# Display the result
print(f"Triangular number {number} is {triangular_number}")

# What triangular number do you want? 10
# Triangular number 10 is 55
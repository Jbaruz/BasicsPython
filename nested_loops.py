# Program to use nested loops to calculate multiple triangular numbers
# Author: JBA
# Date: 27-11-2024

# Loop to ask the user for triangular numbers 5 times
for _ in range(5):
    number = int(input("What triangular number do you want?"))
    triangular_number = sum(range(1, number +1))
    print(f"The triangular number {number} is {triangular_number}\n")

"""
What triangular number do you want?50
The triangular number 50 is 1275
...
...
"""
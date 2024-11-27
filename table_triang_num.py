# Program to generate a table of triangular numbers
# Author: JBA
# Date: 27-11-2024
from eight_triang_num import triangular_number

# Display table header
print("TABLE OF TRIANGULAR NUMBERS")
print("n      Sum from 1 to n")
print("----   ----------------")

# Generate triangular numbers
for n in range(1, 11):
    triangular_number = sum(range(1, n +1)) # Sum from 1 to n
    print(f"{n:<3}     {triangular_number:<16}")

"""
TABLE OF TRIANGULAR NUMBERS
n      Sum from 1 to n
----   ----------------
1       1               
2       3               
3       6               
4       10              
5       15              
6       21              
7       28              
8       36              
9       45              
10      55              

"""
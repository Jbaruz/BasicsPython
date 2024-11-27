# Basic conversions in python
# Author: JBA
# Date: 25-11-2024

# Declare variables
f1 = 123.125
f2 = None
i1 = None
i2 = -150

# Perform and display conversions
i1 = int(f1) # Floating-point to integer conversions
print(f"{f1} assigned to an int produces {i1}")

f1 = float(i2) # integer to floating-point conversions
print(f"{i2} assigned to a float produces {f1}")

f1 = i2/100 # Integer divided by integer (float division in Python)
print(f"{i2} divided by 100 produces {f1}")

f2 = i2/100.0 # Integer divided by a float
print(f"{i2} divided by 100.0 produces {f2}")

f2 = float(i2)/100.0 # Explicit type casting (not necessary in Python)
print(f"(float) {i2} divided by 100 produces {f2}")

"""
123.125 assigned to an int produces 123
-150 assigned to a float produces -150.0
-150 divided by 100 produces -1.5
-150 divided by 100.0 produces -1.5
(float) -150 divided by 100 produces -1.5
"""


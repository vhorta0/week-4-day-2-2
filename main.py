# Advanced Problem Set: Delving Deeper with Numbers in Python

#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.
a=3
b=6
c=5
d=4
e=7
print(a+b*(c+d)/a-e)

# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
a=145
b=12
print(a%b)

# Task 3: Raise 7 to the power of 3 and print the result.
a=7
b=3
print(a**3)

#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
a=23
b=89
c=12
d=54
e=92
f=65
g=71
h=13
i=45
# Use the max() and min() functions to find the highest and lowest number respectively.
print(max(a, b, c, d, e , f, g, h, i))
print(min(a, b, c, d, e , f, g, h, i))
# Task 5: Round the number 12.5678 to 2 decimal places.
a=12.5678
print(round(a, 2))

# Task 6: Find the absolute value of -45.
a= -45
print(abs(a))

#################### PROBLEM 3: Advanced Math Functions ####################
import math

# Task 7: Using the math library, find the floor value of 15.7.
a=15.7
print(math.floor(a))

# Task 8: Find the ceiling value of 15.2.
a=15.2
print(math.ceil(a))

# Task 9: Calculate the square root of 625.
a=625
print(math.sqrt(a))

#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
a= float(34.56)
a1= float(3)
b= float(45.78)
b1=float(5)
c=float(23.89)
c1=float(2)
d=float(12.34)
d1=float(4)
e=float(78.90)
e2=float(6)
# Calculate the total cost for each item (price multiplied by quantity).
print(a*a1)
print(b*b1)
print(c*c1)
print(d*d1)
print(e*e2)
# Then, find the average cost of all items after rounding it to 2 decimal places.
total=(a*a1)+(b*b1)+(c*c1)+(d*d1)+(e*e2)
print(total/5)

#################### END OF ADVANCED PROBLEM SET ####################

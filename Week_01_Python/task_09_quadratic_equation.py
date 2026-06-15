# Task 9 - Solve Quadratic Equation ax^2 + bx + c = 0

import cmath

a = 1
b = 5
c = 6

# Calculate the discriminant
d = (b ** 2) - (4 * a * c)

# Find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('The solutions are {0} and {1}'.format(sol1, sol2))

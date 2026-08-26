# Write a program to calculate area of an equilateral triangle.

import math
side = float(input("Enter the side length of the equilateral triangle: "))

area = (math.sqrt(3) / 4) * (side ** 2)


print(f"\nArea of the equilateral triangle = {area:.2f}")
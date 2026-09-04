# 4. Check Valid Triangle (Using Sides)
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

# Triangle Inequality Theorem: Sum of any two sides must be greater than the third side
if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
    print("The triangle is Valid.")
else:
    print("The triangle is NOT Valid.")
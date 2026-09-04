# 3. Check Valid Triangle (Using Angles)
a1 = float(input("Enter angle 1: "))
a2 = float(input("Enter angle 2: "))
a3 = float(input("Enter angle 3: "))

if (a1 + a2 + a3 == 180) and (a1 > 0 and a2 > 0 and a3 > 0):
    print("The triangle is Valid.")
else:
    print("The triangle is NOT Valid.")
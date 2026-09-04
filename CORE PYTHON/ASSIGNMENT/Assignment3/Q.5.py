# 5. Type of Triangle (Equilateral, Isosceles, or Scalene)
s1 = float(input("Enter side 1: "))
s2 = float(input("Enter side 2: "))
s3 = float(input("Enter side 3: "))

# First ensure it's a valid triangle
if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
    if s1 == s2 == s3:
        print("Equilateral Triangle")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle.")
# 9. Swap Two Numbers Without Using a Third Variable



a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping:  a = {a}, b = {b}")
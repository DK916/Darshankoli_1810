# Swap Two Numbers Using a Third Variable
# Python
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping logic using a temporary variable
temp = a
a = b
b = temp

print(f"After swapping:  a = {a}, b = {b}")
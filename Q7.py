# Find the Sum of Digits of a Three-Digit Number
# Python
num = int(input("Enter a 3-digit number: "))
original_num = num

# Extract digits using floor division (//) and modulo (%) operators
digit3 = num % 10        # Ones digit
num = num // 10

digit2 = num % 10        # Tens digit
digit1 = num // 10       # Hundreds digit

# Calculate sum using addition operator (+)
digit_sum = digit1 + digit2 + digit3

print(f"The sum of digits of {original_num} is: {digit_sum}")
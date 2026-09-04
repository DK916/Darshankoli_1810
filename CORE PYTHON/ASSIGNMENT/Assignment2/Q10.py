# 10. Reverse a Three-Digit Number
# Python
num = int(input("Enter a 3-digit number: "))
original_num = num

# Extract individual digits
digit3 = num % 10        # Ones digit
num = num // 10

digit2 = num % 10        # Tens digit
digit1 = num // 10       # Hundreds digit

# Reconstruct the reversed number using arithmetic operators
reversed_num = (digit3 * 100) + (digit2 * 10) + digit1

print(f"Reversed number of {original_num} is: {reversed_num}")
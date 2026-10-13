# WAP to check if given number is Perfect Number.

n = int(input("Enter number: "))

sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum = sum + i
    i += 1

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
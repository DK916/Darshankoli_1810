
num = int(input("Enter a number: "))
def check_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    return total == num
print(check_perfect(num))
def checkstrong(num):
    original = num
    total = 0
    num = int(input("Enter a number: "))

    while num > 0:
        digit = num % 10

        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        num = num // 10

    return original == total

    print(checkstrong(num))
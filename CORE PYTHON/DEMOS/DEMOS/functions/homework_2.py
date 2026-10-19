def palindrome(num):
    original = num
    reverse = 0
    
    num = int(input("Enter a number: "))

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

    print(palindrome(num))
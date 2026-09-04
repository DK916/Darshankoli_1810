# Authentication with Captcha
import random

CORRECT_USER = "admin"
CORRECT_PASS = "python123"

username = input("Enter User ID: ")
password = input("Enter Password: ")

if username == CORRECT_USER and password == CORRECT_PASS:
    # Generate a random 4-digit number (1000 to 9999)
    captcha = random.randint(1000, 9999)
    print(f"\nCAPTCHA: {captcha}")
    
    user_captcha = int(input("Enter the CAPTCHA displayed above: "))
    
    if user_captcha == captcha:
        print("Verification Successful! Access Granted.")
    else:
        print("Verification Failed! CAPTCHA mismatch.")
else:
    print("Authentication Failed! Incorrect User ID or Password.")
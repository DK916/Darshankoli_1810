# #1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

correct_id = "Darshan"
correct_password = "1234"

i = 1

while i <= 3:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password")
        
    i += 1

if i > 3:
    print("You have used all 3 attempts")
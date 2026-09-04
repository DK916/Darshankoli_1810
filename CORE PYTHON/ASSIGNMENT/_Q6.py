#Write a Program to input two angles from user and find third angle of the
#triangle

angle1 = int(input("Enter first angle:"))
angle2 = int(input("enter second angle:"))

triangle=  180-(angle1+angle2)
print("triangle:",triangle)
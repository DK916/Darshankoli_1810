# #Test 2
# #Q1.
# year = int(input("Enter a year: "))
# if year % 4 != 0:
#     print(" NOT a Leap year")
# elif year % 100 != 0:
#     print("Leap year")
# elif year % 400 == 0:
#     print("Leap year")
# else:
#     print("NOT a Leap year")
    
    
#Q2.

# num = int(input("Enter 3 digit number: "))

# first = num // 100
# second = (num // 10) % 10
# third = num % 10
# if first == second * 2 and first == third / 2:
#     print("Yes, you have done it")
# else:
#     print("Please try next time")
    
    
    
#Q4.


# length = float(input("Enter length: "))
# height = float(input("Enter height: "))
# rate = float(input("Enter painting rate: "))

# area = 4 * length * height

# total_cost = area * rate

# print("Total area =", area)
# print("Total cost =", total_cost)


#Q.5

num1 = float(input("Enter price 1: "))
num2 = float(input("Enter price 2: "))
num3 = float(input("Enter price 3: "))
num44 = float(input("Enter price 4: "))
num55 = float(input("Enter price 5: "))

total = num1 + num2 + num3 + num4 + num5

gst = total * 18 / 100

bill = total + gst

print("Total =", total)
print("GST =", gst)
print("Final Bill =", bill)
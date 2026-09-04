#  Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9) 
# 1. Take inputs for feet and inches
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

# 2. Convert total distance to inches
total_inches = (feet * 12) + inches

centimeters = total_inches * 2.54
meters = centimeters / 100

print(f"\nDistance in meters: {meters:.2f} m")
print(f"Distance in centimeters: {centimeters:.2f} cm")
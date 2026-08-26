# 1. Take inputs for hours, minutes, and seconds
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# 2. Arithmetic calculation
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# 3. Print the result
print("Total time in seconds =", total_seconds)
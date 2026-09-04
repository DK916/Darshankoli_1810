# 6. Calculate Total Salary of an Employee
Python
# Accept basic salary from user
basic = float(input("Enter basic salary: "))

# Calculate allowances using multiplication operator (*)
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

# Calculate total salary using addition operator (+)
total_salary = basic + da + ta + hra

print(f"Basic Salary: {basic:.2f}")
print(f"DA (10%):     {da:.2f}")
print(f"TA (12%):     {ta:.2f}")
print(f"HRA (15%):    {hra:.2f}")
print("-" * 25)
print(f"Total Salary: {total_salary:.2f}")
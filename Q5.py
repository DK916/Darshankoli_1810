#  WAP to calculate selling price of book based on cost price and discount. 
# 1. Take input for cost price and discount percentage
cost_price = float(input("Enter the cost price of the book: "))
discount_percent = float(input("Enter discount percentage: "))

# 2. Arithmetic calculations
discount_amount = (cost_price * discount_percent) / 100
selling_price = cost_price - discount_amount

# 3. Display the results
print(f"\nDiscount Amount = ₹{discount_amount:.2f}")
print(f"Selling Price   = ₹{selling_price:.2f}")
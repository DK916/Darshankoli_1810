# 11. Minimum Number of Notes for an Amount
amount = int(input("Enter total amount: "))
original_amount = amount

# Available currency denominations
denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

print(f"\nBreakdown for Amount = {original_amount}:")

for note in denominations:
    count = amount // note   # Number of notes using floor division
    amount = amount % note    # Remaining amount using modulo
    
    if count > 0:
        print(f"{note:>3} Notes/Coins : {count}")
        total_notes += count

print("-" * 30)
print(f"Minimum Total Notes Needed: {total_notes}")
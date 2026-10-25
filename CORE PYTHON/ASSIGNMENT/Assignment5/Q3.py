# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passenger=int(input("Enter number of passenger:"))
ticket=int(input("Enter ticket price:"))
total=0

for i in range(passenger):
    age=int(input("Enter Age:"))
    
    if age < 12:
        amount=ticket*70/100
        
    elif age > 59:
        amount=ticket*50/100
    else:
        amount=ticket
        
    total+=amount
print("Total ticket amount:",total)
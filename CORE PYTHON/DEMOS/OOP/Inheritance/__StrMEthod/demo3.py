# Create a Book class using __init__() and __str__().
# Requirements:
# 1. Create a class named Book.
# 2. Store title, author, and price using __init__().
# 3. Define __str__() to return all three values in a readable format.
# 4. Create an object with:
#    - Title: "Python Basics"
#    - Author: "Rahul"
#    - Price: 500
# 5. Print the object.
# Expected Output:
# Title: Python Basics
# Author: Rahul
# Price: 500

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        
    def __str__(self):
        return f"Title:{self.title}\t Author:{self.author}\t Price:{self.price}"
    
b1=Book("Python Basics","Rahul",500)
print(b1)
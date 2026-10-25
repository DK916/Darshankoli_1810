class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
         
         
         
c1= Car("Toyota", 40000)

c1.display()

# c1=Car("toyota",50000)
# c2=Car("Suzuki",20000)

# print(f" brand={c1.brand} \t price={c1.price}\n brand={c2.brand}  price={c2.price}")

# # print(c2.brand)
# # print(c2.price)
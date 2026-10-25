class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def getBrand(self):
        return self.brand

    def setBrand(self, new_brand):
        self.brand = new_brand

    def getPrice(self):
        return self.price

    def setPrice(self, new_price):
        self.price = new_price


class Car(Vehicle):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def getModel(self):
        return self.model

    def setModel(self, new_model):
        self.model = new_model


c1 = Car("Toyota", 500000, "Fortuner")

print(c1.getBrand())
print(c1.getPrice())
print(c1.getModel())

c1.setPrice(550000)
c1.setModel("Fortuner Legender")

print("\nAfter Update:")
print(c1.getPrice())
print(c1.getModel())
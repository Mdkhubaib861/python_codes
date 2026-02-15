class Product:
    def __init__(self, pname, qty, price, rating, discount):
        self.pname = pname
        self.qty = qty
        self.price = price
        self.amount = self.qty * self.price
        self.rating = rating
        self.discount = discount

    def finalamount(self):
        return self.amount - self.amount * self.discount / 100 

    def display(self):
        print(self.pname, self.qty, self.price, self.amount, self.rating, self.discount)
        print("Final Amount:", self.finalamount())

s1 = Product("iPhone", 2, 5000, 4.3, 10)
s1.display()

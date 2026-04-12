class Product:
    def __init__(self):
        self.discr = ""
        self.rate = 0.0
        self.qty = 0
        self.amt = 0.0
        self.disc = 0.0
        self.net = 0.0

    def setData(self, dsr, rt, q):
        self.discr = dsr
        self.rate = rt
        self.qty = q

    def process(self):
        self.amt = self.rate * self.qty
        self.disc = self.amt * 10 / 100
        self.net = self.amt - self.disc

    def printBill(self):
        print("Description :", self.discr)
        print(f"Rate        :{self.rate:12.2f}")
        print(f"Quantity    :{self.qty:12d}")
        print(f"Amount      :{self.amt:12.2f}")
        print(f"Discount    :{self.disc:12.2f}")
        print(f"Net amount  :{self.net:12.2f}")

# Main program (same as Billing class)
product = Product()
product.setData("Notebook 180pg", 56.60, 12)
product.process()
product.printBill()

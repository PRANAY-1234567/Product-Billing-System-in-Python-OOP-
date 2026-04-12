# 🧾 Product Billing System in Python (OOP)

## 📌 Description

This Python program implements a simple **Product Billing System** using **Object-Oriented Programming (OOP)**. It calculates the total amount, applies a discount, and displays a formatted bill.

---

## 🚀 Features

* Defines a `Product` class
* Stores product details (description, rate, quantity)
* Calculates:

  * Total amount
  * Discount (10%)
  * Net amount
* Displays a neatly formatted bill

---

## 🛠️ How It Works

1. A class `Product` is created with attributes:

   * `discr` (description)
   * `rate` (price per item)
   * `qty` (quantity)
   * `amt` (total amount)
   * `disc` (discount)
   * `net` (final amount)

2. Methods:

   * `setData()` → Sets product details
   * `process()` → Calculates:

     * `amt = rate × qty`
     * `disc = 10% of amt`
     * `net = amt - disc`
   * `printBill()` → Displays the bill

3. In the main program:

   * A product is created
   * Data is assigned
   * Bill is calculated and printed

---

## 💻 Code

```python id="b9q3kl"
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


# Main program
product = Product()
product.setData("Notebook 180pg", 56.60, 12)
product.process()
product.printBill()
```

---

## ▶️ Example Output

```id="l0a9sk"
Description : Notebook 180pg
Rate        :       56.60
Quantity    :          12
Amount      :      679.20
Discount    :       67.92
Net amount  :      611.28
```

---

## 📚 Concepts Used

* Class and Object
* Instance variables
* Methods (`setData`, `process`, `printBill`)
* Arithmetic calculations
* String formatting (`f-strings`)

---

## 🎯 Use Case

This program helps beginners understand:

* How billing systems work in real applications
* How to structure calculations using OOP
* How to format output professionally

---

## 🔧 Future Improvements

* Take user input instead of hardcoding values
* Add multiple products (shopping cart system)
* Apply different discount rates
* Generate total bill for multiple items

---

## 📄 License

This project is open-source and free to use.

<img width="635" height="861" alt="image" src="https://github.com/user-attachments/assets/ba4cd9f1-f793-40d9-93f6-555be7762598" />


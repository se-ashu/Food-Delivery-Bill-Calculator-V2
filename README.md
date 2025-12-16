# 🍔 Food Delivery Bill Calculator

A simple Python program to calculate the final bill for food delivery orders.  
This project demonstrates the use of loops, conditionals, and basic arithmetic operations in Python.

---

## 📖 Features
- Interactive menu with food items:
  - Burger – ₹120  
  - Pizza – ₹250  
  - Sandwich – ₹100  
  - Pasta – ₹180  
- Allows multiple item selections with quantity input.
- Automatically calculates:
  - **Total food bill**
  - **Delivery charges** (Free delivery for orders above ₹500, else ₹50)
  - **Discounts** (10% discount for bills above ₹1000)
- Displays a detailed bill summary.

---

## 🖥️ How It Works
1. The program displays a menu of food items.
2. The user selects items and enters quantities.
3. When finished, the user chooses **Exit and Calculate Bill**.
4. The program applies delivery charges and discounts based on the total.
5. A final bill summary is printed.

---

## 📋 Example Output
```
Welcome to Food Delivery Bill Calculator!

Menu:
1. Burger - ₹120
2. Pizza - ₹250
3. Sandwich - ₹100
4. Pasta - ₹180
5. Exit and Calculate Bill
Enter your choice (1-5): 2
Enter quantity: 2

Menu:
...
You got FREE delivery!
You got a 10% discount!

------------------------------
Total Food Bill : ₹500
Delivery Charge : ₹0
Discount        : ₹50.00
------------------------------
Final Amount to Pay: ₹450.00
------------------------------
Thank you for ordering with us!
```

---

## 🚀 Getting Started
### Prerequisites
- Python 3.x installed on your system

### Run the Program
```bash
python food_delivery_bill_calculator.py
```

---

## 📂 Project Structure
```
Food-Delivery-Bill-Calculator/
│
├── food_delivery_bill_calculator.py   # Main program file
└── README.md                          # Project documentation
```

---

## 🎯 Learning Goals
- Practice with **loops** (`while`)
- Use of **conditional statements** (`if-elif-else`)
- Handling **user input**
- Applying **basic arithmetic operations**

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork this repository and submit pull requests with improvements or new features.

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

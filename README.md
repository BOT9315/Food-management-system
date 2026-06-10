# 🍕 Food Ordering System

A simple Python-based terminal food ordering system where customers can select items from a predefined menu, view their order, and get a total bill.

---

## 📁 Project Structure

```
food_order/
│
├── main.py            # Entry point – runs the program
├── utils.py           # Shared data: menu and order storage
├── show_menu.py       # Displays the food menu
├── add_food_item.py   # Adds selected item to the order
├── show_food_item.py  # Shows current order
└── total_bill.py      # Calculates and prints the bill
```

---

## 🍽️ Menu (Predefined)

| # | Item         | Price  |
|---|--------------|--------|
| 1 | Pizza        | $250.0 |
| 2 | Burger       | $100.0 |
| 3 | Pasta        | $180.0 |
| 4 | French Fries | $80.0  |
| 5 | Cold Drink   | $40.0  |

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/food-ordering-system.git
   cd food-ordering-system
   ```

2. Run the program:
   ```bash
   python main.py
   ```

> No external libraries required. Uses Python 3 only.

---

## 💻 Usage

```
Welcome to the Food Management System!
1. Show Menu
2. Add Food Item
3. Show Order
4. Calculate Total Bill
5. Exit
```

- **Option 1** – View the full menu with prices
- **Option 2** – Select an item by number and enter quantity
- **Option 3** – View all items added to your order
- **Option 4** – See itemised bill with grand total
- **Option 5** – Exit the program

---

## 📸 Sample Output

```
----- FOOD MENU -----
1. Pizza        - $250.0
2. Burger       - $100.0
3. Pasta        - $180.0
4. French Fries - $80.0
5. Cold Drink   - $40.0
----------------------

Enter item number from menu: 1
Enter quantity: 2
2 Pizza(s) added to the order.

Bill details:
Pizza: 2 x $250.0 = $500.0
Burger: 3 x $100.0 = $300.0
Total Bill: $800.0
```

---

## 🛠️ Technologies Used

- Python 3
- Modular file structure (no external dependencies)

---

## 📌 Concepts Covered

- Python classes and functions
- Modular programming (separate files per function)
- Shared state via `utils.py`
- User input handling and validation
- Dictionary-based data management

---

## 👨‍💻 Author

**Ankush Kumar**  
@BOT9315
AI / Machine Learning Developer


Made with ❤️ as part of a Python OOP learning exercise.

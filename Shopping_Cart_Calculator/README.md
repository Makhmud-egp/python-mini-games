# 🛒 Shopping Cart Calculator

A simple Python program that simulates a store checkout system.  
Users can select items from a price list, specify quantities, and view the final bill with a total amount.

## 📌 Features
- Add multiple items to your cart.
- Calculates price per item based on quantity.
- Displays a full receipt with a grand total.
- Prevents invalid inputs (like wrong item names or non-numeric quantities).

## 🛠️ How It Works
1. User enters the name of the item they want to buy.
2. Program checks if the item is available.
3. User enters the quantity (kg/bottles/etc.).
4. The program adds the total price for that item to the cart.
5. Typing `done` ends the shopping and prints the bill.

## 📂 Example Run

```bash
# Run the program
python shopping_cart.py

# Example output:
What do you want to buy? (or 'done' to finish): apple
How many kg/bottles of apple?: 2
What do you want to buy? (or 'done' to finish): milk
How many kg/bottles of milk?: 1
What do you want to buy? (or 'done' to finish): done

🛒 Your total bill:
apple: $100
milk: $35
💰 Grand Total: $135

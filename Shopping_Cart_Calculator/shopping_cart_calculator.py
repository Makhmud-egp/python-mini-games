# price list for store items
items = {"apple": 50, 
         "banana": 50, 
         "milk": 35,
         "potato": 10,
         "tomato": 10,
         "lemon": 10,
         "melon": 20,
         "greens": 5,
         "onion": 8,
         "garlic": 35,
         }

# shopping cart
store = {}


while True:
    u_buys = input("What do you want to buy? (or 'done' to finish): ").lower().strip()

    if u_buys == "done":
        break

    if u_buys in items:
        try:
            count = int(input(f"How many kg/bottles of {u_buys}?: "))
            total_price = items[u_buys] * count
            store[u_buys] = store.get(u_buys, 0) + total_price
        except:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Item not available.")


# final bill
print("\n🛒 Your total bill:")
grand_total = 0

for key, value in store.items():
    print(f"{key}: ${value}")
    grand_total += value

print(f"💰 Grand Total: ${grand_total}")

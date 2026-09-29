# ==============================================
# === A WORKING CASH REGISTER WITH INVENTORY ===
# ==============================================

# 1. Identify Inventory of the store

inventory = {"water bottle": 1.00, "doritos": 2.50, "kitkat": 3.00, "banana": 0.50}

# 2. setup the available variables

cart_subtotal = 0.00  # this part is to make sure the starting point for the receipt is 0
tax_rate = 0.10 #tax rate of 10%

# 3. print the cash register terminal to make sure the register is working properly

print("=== CASH REGISTER TERMINAL ===")
print("Items available: water bottle, doritos, kitkat, banana")
print("type 'done' when scanning is finished.\n")

# 4. loop setup for scanning process

while True:
    scanned_item = input("scan item: ").lower()

    if scanned_item == "done":
        break

    if scanned_item in inventory:
        cart_subtotal += inventory[scanned_item] 
        print(f" added {scanned_item}! current subtotal: ${cart_subtotal:.2f}\n") 
    else:
        print("[x] Item not foun!\n")

# 5. final receipt calculation

tax_amount = cart_subtotal * tax_rate
final_price = cart_subtotal + tax_amount

# 6. print the final receipt

print("\n=== FINAL RECEIPT ===")
print("subtotal: $", round(cart_subtotal, 2))
print("tax (10%): $", round(tax_amount, 2))
print("Total Due: $", round(final_price, 2))

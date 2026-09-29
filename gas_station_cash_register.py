# ==============================================
# ==INTERACTIVE CASH REGISTER IN A GAS STATION==
# ==============================================

# 1. Store Inventory 

inventory = {"water bottle": 1.00, "hotdog": 2.50, "doritos": 2.00, "coca cola": 1.50}

# 2. setup the available variables

cart_subtotal = 0.00  #to make sure the starting point of the cart is $0
tax_rate = 0.10 # tax rate of 10%

# 3. print cash register terminal to make sure program working properly

print("===CASH REGISTER TERMINAL===")
print("Items available: water bottle, hotdog, doritos, coca cola")
print("type 'done' when item scanning process finished")

# 4. loop for the scanning process

while True:
    scanned_item = input("scan item: ").lower()

    if scanned_item == "done":
        break

    if scanned_item in inventory:
        cart_subtotal += inventory [scanned_item]
        print(f" added {scanned_item}! current subtotal: ${cart_subtotal:.2f}\n")
    else:
        print(" [x] Item not found")

# 5. final receipt calculation

tax_amount = cart_subtotal * tax_rate
final_price = cart_subtotal + tax_amount

# 6. print out final receipt

print("\n=== RECEIPT===")
print("Subtotal: $", round(cart_subtotal, 2))
print("Tax (10%): $", round(tax_amount, 2))
print("Total Due: $", round(final_price, 2))


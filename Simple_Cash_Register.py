# simple Cash Register Simulation

# 1. setup variables or items that will be purchased
item_name = "banana"
item_price = 0.20
quantity = 10

# 2. tax rate to calculate total price after tax
tax_rate = 0.08

# 3. calculate subtotal
sub_total = item_price * quantity

# 4. calculate subtotal after tax
tax_amount = sub_total * tax_rate

# 5. calculate final price
final_price = sub_total + tax_amount

# 6. print out receipt
print("=== STORE RECEIPT ===")
print("item:", item_name)
print("Quantity:", quantity) 
print("subtotal: $", sub_total)
print("tax: $", tax_amount)
print("total amount due: $", final_price)




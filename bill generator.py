print("===== SHOPPING BILL GENERATOR =====")

n = int(input("Enter number of items: "))

grand_total = 0

for i in range(n):
    print("\nItem", i + 1)

    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    grand_total += total

    print("Total for", name, "=", total)

print("\n***** SHOPPING BILL *****")
print("Grand Total =", grand_total)
print("===================================")
print(" THANK YOU FOR SHOPPING!")
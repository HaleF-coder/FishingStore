import csv

# Stores the fishing products, prices, quantities, and reorder levels.
inventory = {}

# Stores all recorded fishing store sales.
sales = []

# This function loads inventory information from the CSV file.
def load_inventory():
    with open("inventory.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            item = row[0]

            inventory[item] = {
                "price": float(row[1]),
                "qty": int(row[2]),
                "reorder": int(row[3])
            }


# This function saves the current inventory to the CSV file.
def save_inventory():
    with open("inventory.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["item", "price", "qty", "reorder"])

        for item in inventory:
            writer.writerow([
                item,
                inventory[item]["price"],
                inventory[item]["qty"],
                inventory[item]["reorder"]
            ])

# This function loads previous sales from the CSV file.
def load_sales():
    with open("sales.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            sale = {
                "date": row[0],
                "item": row[1],
                "qty": int(row[2]),
                "total": float(row[3])
            }

            sales.append(sale)

# This function saves all recorded sales to the CSV file.
def save_sales():
    with open("sales.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["date", "item", "qty", "total"])

        for sale in sales:
            writer.writerow([
                sale["date"],
                sale["item"],
                sale["qty"],
                sale["total"]
            ])

# This function records a sale and updates inventory.
def record_sale():
    item = input("Enter the product sold: ").lower()

    if item in inventory:
        qty = input("Enter the quantity sold: ")

        if qty.isdigit():
            qty = int(qty)

            if qty > 0 and qty <= inventory[item]["qty"]:
                total = qty * inventory[item]["price"]

                inventory[item]["qty"] = inventory[item]["qty"] - qty

                sale = {
                    "date": input("Enter the sale date (YYYY-MM-DD): "),
                    "item": item,
                    "qty": qty,
                    "total": total
                }

                sales.append(sale)

                print("Sale recorded successfully.")
                print("Sale total: $", round(total, 2))

            else:
                print("Invalid quantity or not enough inventory.")

        else:
            print("Invalid quantity. Enter a whole number.")

    else:
        print("Product not found in inventory.")


# This function displays the main menu options.
def show_menu():
    print("\n===== FISHING STORE INVENTORY MANAGER =====")
    print("1. View inventory")
    print("2. Add or restock an item")
    print("3. Record a sale")
    print("4. Show low-stock alerts")
    print("5. Sales report with charts")
    print("6. Run 30-day simulation")
    print("7. Save and exit")

# This function displays every fishing product and its details.
def view_inventory():
    print("\n===== CURRENT INVENTORY =====")

    for item in inventory:
        print("Product:", item)
        print("Price: $", inventory[item]["price"])
        print("Quantity:", inventory[item]["qty"])
        print("Reorder Level:", inventory[item]["reorder"])
        print("-----------------------------")

# This function adds a new product or updates an existing product.
def add_item():
    item = input("Enter the product name: ").lower()

    if item in inventory:
        print("Current quantity:", inventory[item]["qty"])
        amount = input("Enter the quantity to add: ")

        if amount.isdigit():
            inventory[item]["qty"] = inventory[item]["qty"] + int(amount)
            print("Inventory updated successfully.")
        else:
            print("Invalid quantity. Please enter a whole number.")

    else:
        price = input("Enter the product price: ")
        qty = input("Enter the starting quantity: ")
        reorder = input("Enter the reorder level: ")

        if price.replace(".", "", 1).isdigit() and qty.isdigit() and reorder.isdigit():
            inventory[item] = {
                "price": float(price),
                "qty": int(qty),
                "reorder": int(reorder)
            }
            print("New product added successfully.")
        else:
            print("Invalid information. Please enter valid numbers.")

# This function runs the main menu until the user chooses to exit.
def main():
    choice = ""

    while choice != "7":
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "7":
             save_inventory()
             save_sales()
             print("Saving data and exiting the program. Goodbye!")

        elif choice == "1":
            view_inventory()

        elif choice == "2":
            add_item()

        elif choice == "3":
            record_sale()

        elif choice == "4":
            print("Coming soon")

        elif choice == "5":
            print("Coming soon")

        elif choice == "6":
            print("Coming soon")

        else:
            print("Invalid choice. Please select an option from 1 to 7.")


load_inventory()
load_sales()
main()

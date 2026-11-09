# Stores the fishing products, prices, quantities, and reorder levels.
inventory = {
    "fishing lure": {"price": 6.99, "qty": 25, "reorder": 8},
    "fishing line": {"price": 9.99, "qty": 15, "reorder": 5},
    "hooks": {"price": 4.99, "qty": 30, "reorder": 10}
}

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

# This function runs the main menu until the user chooses to exit.
def main():
    choice = ""

    while choice != "7":
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "7":
            print("Saving data and exiting the program. Goodbye!")

        elif choice == "1":
            view_inventory()

        elif choice == "2":
            print("Coming soon")

        elif choice == "3":
            print("Coming soon")

        elif choice == "4":
            print("Coming soon")

        elif choice == "5":
            print("Coming soon")

        elif choice == "6":
            print("Coming soon")

        else:
            print("Invalid choice. Please select an option from 1 to 7.")


main()

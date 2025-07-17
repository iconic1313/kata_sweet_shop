from services.sweet_service import SweetService

def display_sweets(sweets):
    print("\nAvailable Sweets:")
    for s in sweets:
        print(f"{s.id}: {s.name} | {s.category} | ₹{s.price} | Qty: {s.quantity}")
    print()

def main():
    service = SweetService()
    while True:
        print("\n ______kata Sweet Shop______")
        print("1. Add Sweet")
        print("2. View Sweets")
        print("3. Purchase Sweet")
        print("4. Restock Sweet")
        print("5. Delete Sweet")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            sweet = service.add_sweet(name, category, price, quantity)
            print(f" Sweet added: {sweet}")

        elif choice == "2":
            display_sweets(service.get_all_sweets())

        elif choice == "3":
            sweet_id = int(input("Sweet ID to purchase: "))
            qty = int(input("Quantity: "))
            try:
                service.purchase_sweet(sweet_id, qty)
                print(" Purchased.")
            except ValueError as e:
                print("no", e)

        elif choice == "4":
            sweet_id = int(input("Sweet ID to restock: "))
            qty = int(input("Quantity: "))
            try:
                service.restock_sweet(sweet_id, qty)
                print(" Restocked done")
            except ValueError as e:
                print("", e)

        elif choice == "5":
            sweet_id = int(input("Sweet id to delete: "))
            service.delete_sweet(sweet_id)
            print(" Deleted.")

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()

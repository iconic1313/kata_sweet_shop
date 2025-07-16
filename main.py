from models.sweet import Sweet
from services.sweet_service import SweetService

def display_sweets(sweets):
    print("\nAvailable Sweets:")
    for s in sweets:
        print(f"{s.id}: {s.name} | {s.category} | ₹{s.price} | Qty: {s.quantity}")
    print()

def main():
    service = SweetService()

    # Sample data
    service.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
    service.add_sweet(Sweet(1002, "Gulab Jamun", "Milk-Based", 10, 50))
    service.add_sweet(Sweet(1003, "Gajar Halwa", "Vegetable-Based", 30, 15))

    display_sweets(service.get_all_sweets())

    # Purchase
    service.purchase_sweet(1002, 5)
    print("Purchased 5 Gulab Jamun.\n")

    # Restock
    service.restock_sweet(1003, 10)
    print("Restocked 10 Gajar Halwa.\n")

    # Search
    results = service.search_sweets(category="milk")
    print("Search results for category='milk':")
    display_sweets(results)

    # Sort
    sorted_by_price = service.sort_sweets("price")
    print("Sweets sorted by price:")
    display_sweets(sorted_by_price)

if __name__ == "__main__":
    main()

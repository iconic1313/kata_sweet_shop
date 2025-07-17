from typing import List, Optional
from models.sweet import Sweet

class SweetService:
    def __init__(self):
        self.sweets: List[Sweet] = []

    def add_sweet(self, name, category, price, quantity):
        sweet = Sweet(name, category, price, quantity)
        self.sweets.append(sweet)
        return sweet

    def delete_sweet(self, sweet_id: int):
        self.sweets = [s for s in self.sweets if s.id != sweet_id]

    def get_all_sweets(self) -> List[Sweet]:
        return self.sweets

    def search_sweets(self, name: Optional[str] = None, category: Optional[str] = None,
                      price_range: Optional[tuple] = None) -> List[Sweet]:
        result = self.sweets
        if name:
            result = [s for s in result if name.lower() in s.name.lower()]
        if category:
            result = [s for s in result if category.lower() in s.category.lower()]
        if price_range:
            min_price, max_price = price_range
            result = [s for s in result if min_price <= s.price <= max_price]
        return result

    def sort_sweets(self, key: str) -> List[Sweet]:
        if key not in ('name', 'price', 'category'):
            raise ValueError("Can only sort by name, price, or category")
        return sorted(self.sweets, key=lambda s: getattr(s, key))

    def purchase_sweet(self, sweet_id: int, quantity: int):
        for s in self.sweets:
            if s.id == sweet_id:
                if s.quantity < quantity:
                    raise ValueError("Not enough stock available")
                s.quantity -= quantity
                return
        raise ValueError("Sweet not found")

    def restock_sweet(self, sweet_id: int, quantity: int):
        for s in self.sweets:
            if s.id == sweet_id:
                s.quantity += quantity
                return
        raise ValueError("Sweet not found")

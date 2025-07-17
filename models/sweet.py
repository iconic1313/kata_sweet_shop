from dataclasses import dataclass

@dataclass
class Sweet:
   
    _id_counter = 1

    def __init__(self, name, category, price, quantity):
        self.id = Sweet._id_counter
        Sweet._id_counter += 1
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id}: {self.name} | {self.category} | ₹{self.price} | Qty: {self.quantity}"


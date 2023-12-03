"""This module handles orders within the system"""
from dataclasses import dataclass, field


@dataclass
class Order:
    """An Order within the system"""

    items: list[str] = field(default_factory=list)
    quantites: list[int] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    status: str = field(default="open", init=False)

    def add_item(self, name: str, quantity: int, price: int) -> None:
        """Adds an item to the order"""
        self.items.append(name)
        self.quantites.append(quantity)
        self.prices.append(price)

    def total_price(self) -> int:
        """Calculates and returns the total price of the order"""
        return sum([quantity * price for quantity, price in zip(self.quantites, self.prices)])

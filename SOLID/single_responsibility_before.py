"""
This file goes over the S in SOLID Design principles

S: Single Responsibility
    O: Open/Closed
    L: Liskov Substitution
    I: Interface Segregation
    D: Dependency Inversion

A module should be responsible to one, and only one, actor.

Below we can see that the Order class has 2 responsibilities.
Managing the items within the order and paying for the items.

add_item and total_price can resonably be grouped into "Managing".
pay is just paying for the order and isn't related to managing the items.

This breaks the Single Responsibility principle.

"""
from dataclasses import dataclass, field


@dataclass
class Order:
    """An Order within the system"""

    items: list[str] = field(default_factory=list)
    quantites: list[int] = field(default_factory=list)
    prices: list[int] = field(default_factory=list)
    status: str = field(default="Open", init=False)

    def add_item(self, name: str, quantity: int, price: int) -> None:
        """Adds an item to the order"""
        self.items.append(name)
        self.quantites.append(quantity)
        self.prices.append(price)

    def total_price(self) -> int:
        """Calculates and returns the total price of the order"""
        return sum([quantity * price for quantity, price in zip(self.quantites, self.prices)])

    def pay(self, payment_type: str, security_code: str) -> None:
        """Execute payment for the current order"""
        if payment_type == "debit":
            print("processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"unknown payment type: {payment_type}")

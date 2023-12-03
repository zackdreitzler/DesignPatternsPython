"""
This file goes over the O in SOLID Design principles

    S: Single Responsibility
O: Open/Closed
    L: Liskov Substitution
    I: Interface Segregation
    D: Dependency Inversion

Here we see that the PaymentProcessor class violates the open closed principle.
We can see this because to add another payment type, the class would need changes.

"""
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


class PaymentProcessor:
    """Process the payment of a given order"""

    def pay_debit(self, order: Order, security_code: str) -> None:
        """Pay the order with debit card"""
        print("processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order: Order, security_code: str) -> None:
        """Pay the order with a credit card"""
        print("processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

"""
This file goes over the O in SOLID Design principles

    S: Single Responsibility
O: Open/Closed
    L: Liskov Substitution
    I: Interface Segregation
    D: Dependency Inversion

"software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification"

This file follows the open closed principle because we have refactored
PaymentProcessor to an interface. It is now closed to modification but
can be extended with subclasses.

"""
from abc import ABC, abstractmethod
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


class PaymentProcessor(ABC):
    """Process the payment of a given order"""

    @abstractmethod
    def pay(self, order: Order, security_code: str) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    """Processes payments with debit cards"""

    def pay(self, order: Order, security_code: str) -> None:
        """Pay the order with debit card"""
        print("processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    """Processes payments with credit cards"""

    def pay(self, order: Order, security_code: str) -> None:
        """Pay the order with a credit card"""
        print("processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

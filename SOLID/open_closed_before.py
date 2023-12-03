"""
This file goes over the O in SOLID Design principles

    S: Single Responsibility
O: Open/Closed
    L: Liskov Substitution
    I: Interface Segregation
    D: Dependency Inversion

"software entities (classes, modules, functions, etc.)
should be open for extension, but closed for modification"

Here we see that the PaymentProcessor class violates the open closed principle.
We can see this because to add another payment type, the class would need changes.

"""
from SOLID.order import Order


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

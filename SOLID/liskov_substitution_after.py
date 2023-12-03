"""
This file goes over the L in SOLID Design principles

    S: Single Responsibility
    O: Open/Closed
L: Liskov Substitution
    I: Interface Segregation
    D: Dependency Inversion

Subtype Requirement: Let phi(x) be a property provable about objects x of type T.
Then phi(y) should be true for objects y of type S where S is a subtype of T.

Simplified: objects of a superclass shall be replaceable with objects of its subclasses
without breaking the application

This no longer fails the Liskov principle because we have moved the security_code
to the subclasses. So any subclass can be swapped with the superclass and the
application would still work.

"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from SOLID.order import Order


class PaymentProcessor(ABC):
    """Process the payment of a given order"""

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


@dataclass
class DebitPaymentProcessor(PaymentProcessor):
    """Processes payments with debit cards"""

    security_code: str

    def pay(self, order: Order) -> None:
        """Pay the order with debit card"""
        print("processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


@dataclass
class CreditPaymentProcessor(PaymentProcessor):
    """Processes payments with credit cards"""

    security_code: str

    def pay(self, order: Order) -> None:
        """Pay the order with a credit card"""
        print("processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


@dataclass
class PaypalPaymentProcessor(PaymentProcessor):
    """Processes payments with a paypal account"""

    email_address: str

    def pay(self, order: Order) -> None:
        """Pay the order with an email"""
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

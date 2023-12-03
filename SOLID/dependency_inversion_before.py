"""
This file goes over the L in SOLID Design principles

    S: Single Responsibility
    O: Open/Closed
    L: Liskov Substitution
    I: Interface Segregation
D: Dependency Inversion

A: High-level modules should not import anything from low-level modules.
   Both should depend on abstractions (e.g., interfaces).
B: Abstractions should not depend on details. Details (concrete implementations)
   should depend on abstractions.

This file breaks that princple through the SMSAuthorizer. This is a specific
type of authorizer. To not break this principle, there should be an interface
not a class implementation.

"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from SOLID.order import Order


class PaymentProcessor(ABC):
    """Process the payment of a given order"""

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


@dataclass
class SMSAuthorizer:
    """Authorize through SMS"""

    authorized: bool = field(default=False)

    def verify_code(self, code) -> None:
        """Verifys the provided code"""
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        """Returns true if the caller is authorized"""
        return self.authorized


@dataclass
class DebitPaymentProcessor(PaymentProcessor):
    """Processes payments with debit cards"""

    security_code: str
    authorizer: SMSAuthorizer

    def pay(self, order: Order) -> None:
        """Pay the order with debit card"""
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
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
    authorizer: SMSAuthorizer

    def pay(self, order: Order) -> None:
        """Pay the order with an email"""
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

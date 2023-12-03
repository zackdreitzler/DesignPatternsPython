"""
This file goes over the L in SOLID Design principles

    S: Single Responsibility
    O: Open/Closed
    L: Liskov Substitution
I: Interface Segregation
    D: Dependency Inversion

No code should be forced to depend on methods it does not use.

This fails this principle because CreditCardPaymentProcessor does
not need to implement the auth_sms function.

"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from SOLID.order import Order


class PaymentProcessor(ABC):
    """Process the payment of a given order"""

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order: Order) -> None:
        pass


@dataclass
class DebitPaymentProcessor(PaymentProcessor):
    """Processes payments with debit cards"""

    security_code: str
    verified: bool = field(default=False)

    def auth_sms(self, code: str) -> None:
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        """Pay the order with debit card"""
        if not self.verified:
            raise Exception("Not authorized")
        print("processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


@dataclass
class CreditPaymentProcessor(PaymentProcessor):
    """Processes payments with credit cards"""

    security_code: str
    verified: bool = field(default=False)

    def auth_sms(self, code: str) -> None:
        raise Exception("Credit card payments do not support SMS code authorization!")

    def pay(self, order: Order) -> None:
        """Pay the order with a credit card"""
        if not self.verified:
            raise Exception("Not authorized")
        print("processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


@dataclass
class PaypalPaymentProcessor(PaymentProcessor):
    """Processes payments with a paypal account"""

    email_address: str
    verified: bool = field(default=False)

    def auth_sms(self, code: str) -> None:
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order: Order) -> None:
        """Pay the order with an email"""
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

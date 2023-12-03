"""
This file goes over the L in SOLID Design principles

    S: Single Responsibility
    O: Open/Closed
    L: Liskov Substitution
I: Interface Segregation
    D: Dependency Inversion

No code should be forced to depend on methods it does not use.

This passes the principle because we have created the SMSAuthorizer 
class. This can then be passed to any PaymentProcessor subclass that
requires it. We did a Composition approach here. Another option would
have been to create the PaymentProcessorSMS class and have the necessary
subclasses inherit from that class.

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

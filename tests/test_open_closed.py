"""This module tests the functionality of the SOLID files"""
import pytest

from SOLID.open_closed_after import CreditPaymentProcessor, DebitPaymentProcessor, Order


@pytest.fixture
def valid_order() -> Order:
    items: list[str] = ["Keyboard", "Monitor"]
    quantites: list[int] = [1, 2]
    prices: list[int] = [50, 65]

    return Order(items, quantites, prices)


@pytest.fixture
def empty_order() -> Order:
    return Order()


@pytest.fixture
def credit_payment_processor() -> CreditPaymentProcessor:
    return CreditPaymentProcessor()


@pytest.fixture
def debit_payment_processor() -> DebitPaymentProcessor:
    return DebitPaymentProcessor()


class TestCreditPaymentProcessor:
    """Test the functionality of the CreditPaymentProcessor class"""

    def test_paying_for_nonempty_order(self, valid_order, credit_payment_processor):
        """Test paying an order with a debit card"""
        credit_payment_processor.pay(valid_order, "123456")

        assert valid_order.status == "paid"

    def test_paying_for_empty_order(self, empty_order, credit_payment_processor):
        """Test paying an order with a debit card"""
        credit_payment_processor.pay(empty_order, "123456")

        assert empty_order.status == "paid"


class TestDebitPaymentProcessor:
    """Test the functionality of the DebitPaymentProcessor class"""

    def test_paying_for_nonempty_order(self, valid_order, debit_payment_processor):
        """Test paying an order with a debit card"""
        debit_payment_processor.pay(valid_order, "123456")

        assert valid_order.status == "paid"

    def test_paying_for_empty_order(self, empty_order, credit_payment_processor):
        """Test paying an order with a credit card"""
        credit_payment_processor.pay(empty_order, "123456")

        assert empty_order.status == "paid"

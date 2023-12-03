"""This module tests the functionality of the SOLID files"""
import pytest

from SOLID.liskov_substitution_after import (
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    Order,
    PaypalPaymentProcessor,
)


@pytest.fixture
def valid_order() -> Order:
    items: list[str] = ["Keyboard", "Monitor"]
    quantites: list[int] = [1, 2]
    prices: list[int] = [50, 65]

    return Order(items, quantites, prices)


@pytest.fixture
def empty_order() -> Order:
    return Order()


class TestOrder:
    """Test the functionality of the Order class"""

    def test_adding_item_to_nonempty_order(self, valid_order):
        """Test adding an item to a nonempty order"""
        my_order: Order = valid_order
        my_order.add_item("Mouse", 1, 25)

        assert "Mouse" in my_order.items
        assert 1 in my_order.quantites
        assert len(my_order.quantites) == 3
        assert 25 in my_order.prices
        assert len(my_order.prices) == 3

    def test_adding_item_to_empty_order(self, empty_order):
        """Test adding an item to an empty order"""
        my_order: Order = empty_order
        my_order.add_item("Mouse", 1, 25)

        assert "Mouse" in my_order.items
        assert 1 in my_order.quantites
        assert len(my_order.quantites) == 1
        assert 25 in my_order.prices
        assert len(my_order.prices) == 1

    def test_getting_total_price_with_nonempty_order(self, valid_order):
        """Test getting the total price of a nonempty order"""
        assert valid_order.total_price() == 180

    def test_getting_total_price_with_empty_order(self, empty_order):
        """Test getting the total price of an empty order"""
        assert empty_order.total_price() == 0


@pytest.fixture
def credit_payment_processor() -> CreditPaymentProcessor:
    return CreditPaymentProcessor("1234567")


@pytest.fixture
def debit_payment_processor() -> DebitPaymentProcessor:
    return DebitPaymentProcessor("1234567")


@pytest.fixture
def paypal_payment_processor() -> PaypalPaymentProcessor:
    return PaypalPaymentProcessor("payment@example.com")


class TestCreditPaymentProcessor:
    """Test the functionality of the CreditPaymentProcessor class"""

    def test_paying_for_nonempty_order(self, valid_order, credit_payment_processor):
        """Test paying an order with a debit card"""
        credit_payment_processor.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_empty_order(self, empty_order, credit_payment_processor):
        """Test paying an order with a debit card"""
        credit_payment_processor.pay(empty_order)

        assert empty_order.status == "paid"


class TestDebitPaymentProcessor:
    """Test the functionality of the DebitPaymentProcessor class"""

    def test_paying_for_nonempty_order(self, valid_order, debit_payment_processor):
        """Test paying an order with a debit card"""
        debit_payment_processor.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_empty_order(self, empty_order, debit_payment_processor):
        """Test paying an order with a credit card"""
        debit_payment_processor.pay(empty_order)

        assert empty_order.status == "paid"


class TestPaypalPaymentProcessor:
    """Test the functionality of the PaypalPaymentProcessor class"""

    def test_paying_for_nonempty_order(self, valid_order, paypal_payment_processor):
        """Test paying an order with a paypal account"""
        paypal_payment_processor.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_empty_order(self, empty_order, paypal_payment_processor):
        """Test paying an order with a paypal account"""
        paypal_payment_processor.pay(empty_order)

        assert empty_order.status == "paid"

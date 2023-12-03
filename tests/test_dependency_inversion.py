"""This module tests the functionality of the SOLID files"""
import pytest

from SOLID.dependency_inversion_after import (
    AuthorizerGoogle,
    AuthorizerSMS,
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


@pytest.fixture
def credit_payment_processor() -> CreditPaymentProcessor:
    return CreditPaymentProcessor("1234567")


@pytest.fixture
def sms_authorizer() -> AuthorizerSMS:
    return AuthorizerSMS()


@pytest.fixture
def google_authorizer() -> AuthorizerGoogle:
    return AuthorizerGoogle()


@pytest.fixture
def debit_payment_processor_not_authorized_sms(sms_authorizer) -> DebitPaymentProcessor:
    return DebitPaymentProcessor("1234567", sms_authorizer)


@pytest.fixture
def debit_payment_processor_authorized_sms(sms_authorizer) -> DebitPaymentProcessor:
    security_code: str = "1234567"
    debit = DebitPaymentProcessor("1234567", sms_authorizer)
    debit.authorizer.verify_code(security_code)
    return debit


@pytest.fixture
def debit_payment_processor_not_authorized_google(google_authorizer) -> DebitPaymentProcessor:
    return DebitPaymentProcessor("1234567", google_authorizer)


@pytest.fixture
def debit_payment_processor_authorized_google(google_authorizer) -> DebitPaymentProcessor:
    security_code: str = "1234567"
    debit = DebitPaymentProcessor("1234567", google_authorizer)
    debit.authorizer.verify_code(security_code)
    return debit


@pytest.fixture
def paypal_payment_processor_not_authorized_sms(sms_authorizer) -> PaypalPaymentProcessor:
    return PaypalPaymentProcessor("payment@example.com", sms_authorizer)


@pytest.fixture
def paypal_payment_processor_authorized_sms(sms_authorizer) -> PaypalPaymentProcessor:
    paypay_email: str = "payment@example.com"
    paypal: PaypalPaymentProcessor = PaypalPaymentProcessor(paypay_email, sms_authorizer)
    paypal.authorizer.verify_code(paypay_email)
    return paypal


@pytest.fixture
def paypal_payment_processor_not_authorized_google(google_authorizer) -> PaypalPaymentProcessor:
    return PaypalPaymentProcessor("payment@example.com", google_authorizer)


@pytest.fixture
def paypal_payment_processor_authorized_google(google_authorizer) -> PaypalPaymentProcessor:
    paypay_email: str = "payment@example.com"
    paypal: PaypalPaymentProcessor = PaypalPaymentProcessor(paypay_email, google_authorizer)
    paypal.authorizer.verify_code(paypay_email)
    return paypal


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

    def test_paying_for_nonempty_order_authorized_sms(
        self, valid_order, debit_payment_processor_authorized_sms
    ):
        """Test paying an order with a debit card"""
        debit_payment_processor_authorized_sms.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_nonempty_order_not_authorized_sms(
        self, valid_order, debit_payment_processor_not_authorized_sms
    ):
        """Test paying an order with a debit card"""
        with pytest.raises(Exception) as unverified:
            debit_payment_processor_not_authorized_sms.pay(valid_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_empty_order_authorized_sms(
        self, empty_order, debit_payment_processor_authorized_sms
    ):
        """Test paying an order with a credit card"""
        debit_payment_processor_authorized_sms.pay(empty_order)

        assert empty_order.status == "paid"

    def test_paying_for_empty_order_not_authorized_sms(
        self, empty_order, debit_payment_processor_not_authorized_sms
    ):
        """Test paying an order with a debit card"""
        with pytest.raises(Exception) as unverified:
            debit_payment_processor_not_authorized_sms.pay(empty_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_nonempty_order_authorized_google(
        self, valid_order, debit_payment_processor_authorized_google
    ):
        """Test paying an order with a debit card"""
        debit_payment_processor_authorized_google.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_nonempty_order_not_authorized_google(
        self, valid_order, debit_payment_processor_not_authorized_google
    ):
        """Test paying an order with a debit card"""
        with pytest.raises(Exception) as unverified:
            debit_payment_processor_not_authorized_google.pay(valid_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_empty_order_authorized_google(
        self, empty_order, debit_payment_processor_authorized_google
    ):
        """Test paying an order with a credit card"""
        debit_payment_processor_authorized_google.pay(empty_order)

        assert empty_order.status == "paid"

    def test_paying_for_empty_order_not_authorized_google(
        self, empty_order, debit_payment_processor_not_authorized_google
    ):
        """Test paying an order with a debit card"""
        with pytest.raises(Exception) as unverified:
            debit_payment_processor_not_authorized_google.pay(empty_order)

        assert str(unverified.value) == "Not authorized"


class TestPaypalPaymentProcessor:
    """Test the functionality of the PaypalPaymentProcessor class"""

    def test_paying_for_nonempty_order_authorized_sms(
        self, valid_order, paypal_payment_processor_authorized_sms
    ):
        """Test paying an order with paypal"""
        paypal_payment_processor_authorized_sms.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_nonempty_order_not_authorized_sms(
        self, valid_order, paypal_payment_processor_not_authorized_sms
    ):
        """Test paying an order with paypal"""
        with pytest.raises(Exception) as unverified:
            paypal_payment_processor_not_authorized_sms.pay(valid_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_empty_order_authorized_sms(
        self, empty_order, paypal_payment_processor_authorized_sms
    ):
        """Test paying an order with paypal"""
        paypal_payment_processor_authorized_sms.pay(empty_order)

        assert empty_order.status == "paid"

    def test_paying_for_empty_order_not_authorized_sms(
        self, empty_order, paypal_payment_processor_not_authorized_sms
    ):
        """Test paying an order with paypal"""
        with pytest.raises(Exception) as unverified:
            paypal_payment_processor_not_authorized_sms.pay(empty_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_nonempty_order_authorized_google(
        self, valid_order, paypal_payment_processor_authorized_google
    ):
        """Test paying an order with paypal"""
        paypal_payment_processor_authorized_google.pay(valid_order)

        assert valid_order.status == "paid"

    def test_paying_for_nonempty_order_not_authorized_google(
        self, valid_order, paypal_payment_processor_not_authorized_google
    ):
        """Test paying an order with paypal"""
        with pytest.raises(Exception) as unverified:
            paypal_payment_processor_not_authorized_google.pay(valid_order)

        assert str(unverified.value) == "Not authorized"

    def test_paying_for_empty_order_authorized_google(
        self, empty_order, paypal_payment_processor_authorized_google
    ):
        """Test paying an order with paypal"""
        paypal_payment_processor_authorized_google.pay(empty_order)

        assert empty_order.status == "paid"

    def test_paying_for_empty_order_not_authorized_google(
        self, empty_order, paypal_payment_processor_not_authorized_google
    ):
        """Test paying an order with paypal"""
        with pytest.raises(Exception) as unverified:
            paypal_payment_processor_not_authorized_google.pay(empty_order)

        assert str(unverified.value) == "Not authorized"

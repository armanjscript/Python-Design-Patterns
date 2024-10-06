from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process(self):
        pass
    
    
class CreditCardPayment(Payment):
    def process(self):
        return "Processing credit card payment..."

class PaypalPayment(Payment):
    def process(self):
        return "Processing paypal payment..."

class BankTransferPayement(Payment):
    def process(self):
        return "Processing BankTransferPayement payment..."
    

class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self):
        pass

class CreditCardPaymentFactory(PaymentFactory):
    def create_payment(self):
        return CreditCardPayment()


class PaypalPaymentFactory(PaymentFactory):
    def create_payment(self):
        return PaypalPayment()


class BankTransferPaymentFactory(PaymentFactory):
    def create_payment(self):
        return BankTransferPayement()
    

#Client code
def get_payment_factory(factory):
    return factory.create_payment()


if __name__ == "__main__":
    payment_type = "Paypal"
    factories = {
        "CreditCard": CreditCardPaymentFactory(),
        "Paypal": PaypalPaymentFactory(),
        "BankTransfer": BankTransferPaymentFactory(),
    }
    
    payment_method = get_payment_factory(factories.get(payment_type))
    print(payment_method.process())
    
    
       
    

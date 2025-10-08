# abstraction
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} SAR in cash")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f" Paid {amount} SAR using card")

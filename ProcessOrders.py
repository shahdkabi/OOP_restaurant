# polymorphism

from Orders import DineInOrder, DeliveryOrder
from Customer import Customer
from PaymentMethod import CashPayment, CardPayment

# Create customers
shahd = Customer("Shahd", 500)
hosam = Customer("Hosam", 300)

# Create orders
orders = [
    DineInOrder(shahd, [("Burger", 50), ("Fries", 20)], table_number=5),
    DeliveryOrder(hosam, [("Pizza", 80), ("Soda", 10)], address="Riyadh - Olaya")
]

# payment methods
payments = [CashPayment(), CardPayment()]

# inheritance
from Customer import Customer

class Order:
    def __init__(self, customer: Customer, items):
        self.customer = customer
        self.items = items  #the orders

    def calculate_total(self):
        return sum(price for item, price in self.items)

    def summary(self):
        print(f"Order for {self.customer.get_name()} with items {self.items}")

class DineInOrder(Order):
    def __init__(self, customer, items, table_number):
        super().__init__(customer, items)
        self.table_number = table_number

    def summary(self):
        print(f"Dine-in order at table {self.table_number} for {self.customer.get_name()}. Total: {self.calculate_total()} SAR")

class DeliveryOrder(Order):
    def __init__(self, customer, items, address):
        super().__init__(customer, items)
        self.address = address

    def summary(self):
        print(f"Delivery order to {self.address} for {self.customer.get_name()}. Total: {self.calculate_total()} SAR")

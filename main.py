# main
#Call all files and run the code
from ProcessOrders import orders, payments

print("=== Welcome to Our Restaurant System ===\n")

for order, payment in zip(orders, payments):
    order.summary()
    total = order.calculate_total()
    payment.pay(total)
    order.customer.spend(total)
    print("-----")
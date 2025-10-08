# Encapsulation
class Customer:
    def __init__(self, name, balance):
        self.__name = name        # private
        self.__balance = balance  # private

    # Getter
    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    # Setter
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit")

    def spend(self, amount):
        if 0 < amount <= self.__balance:
            original_balance = self.__balance
            self.__balance -= amount
            return original_balance, self.__balance  # return before/after balances
        else:
            return None, None  # indicate insufficient funds

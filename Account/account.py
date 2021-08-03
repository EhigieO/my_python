# class Account:
#     def __init__(self, name: str, number: str, pin: str, acct_type: str) -> None:
#         self.name: str = name
#         self.number = number
#         self.balance = 0.0
#         self.pin = pin
#         self.type = acct_type
#
#     def withdraw(self, amount: float, pin: str) -> None:
#         if amount < 0:
#             raise NegativeAmountEror
#
#         if self.balance < amount:
#             raise Exception("Amount can't withdraw negative amount")
#
#         if self.balance >= amount:
#             self.balance -= amount
#
#     def deposit(self, amount: float) -> None:
#         pass
#
#     def transfer(self, account_number: str, amount: float, pin: str) -> None:
#         pass
#
#     def change_pin(self, old_pin: str, new_pin: str) -> None:
#         pass
#

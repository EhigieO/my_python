# import unittest
# from account import Account
#
#
# class MyTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.account1 = Account("name", "0123456789", "1234", "savings")
#
#     def test_something(self):
#         self.assertEqual(True, True)
#
#     def test_account1_has_number(self):
#         self.assertIsNotNone(self.account1.number)
#         self.assertIsInstance(self.account1.number, str)
#
#     def test_account1_has_name(self):
#         self.assertIsNotNone(self.account1.name)
#         self.assertIsInstance(self.account1.name, str)
#
#     def test_account1_has_balance(self):
#         self.assertIsNotNone(self.account1.balance)
#         self.assertIsInstance(self.account1.balance, float)
#
#     def test_account1_has_pin(self):
#         self.assertIsNotNone(self.account1.pin)
#         self.assertIsInstance(self.account1.pin, str)
#
#     def test_account1_has_type(self):
#         self.assertIsNotNone(self.account1.type)
#         self.assertIsInstance(self.account1.type, str)
#
#     def test_account1_can_withdraw(self):
#         self.account1.withdraw(0.0, "1234")
#
#     def test_account1_cant_withdraw_negative_amount(self):
#
#     def test_account1_cant_withdraw_above_balance(self):
#         self.assertRaises(Exception, self.account1.withdraw, (10.0, "1234"))
#         self.assertIsInstance(self.account1.type, str)
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest

from pythonClasses.number_operations import get_length


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()


    def test_get_length(self):
        result = get_length([1, 2, 1])
        self.assertEqual(result, 3)

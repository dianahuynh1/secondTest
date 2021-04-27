import unittest
from py.calc import add_one, minus_one


class TestCalc(unittest.TestCase):
    def add_one_should_return_two(self):
        self.assertEqual(2, add_one(1))

    def minus_one_should_return_three(self):
        self.assertEqual(3, minus_one(4))


if __name__ == '__main__':
    unittest.main()

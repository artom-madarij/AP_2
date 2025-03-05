import unittest
from lab1 import func

class Test(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func([1, 2, 3, 4, 5]), 0)

    def test_func_2(self):
        self.assertEqual(func([6, 5, 4, 3, 2, 1]), 0)

    def test_func_3(self):
        self.assertEqual(func([1, 2]), 0)

    def test_func_4(self):
        self.assertEqual(func([2, 3, 1, 4, 5, 1, 4, 8, 9, 2]), 5)

if __name__ == '__main__':
    unittest.main()

import unittest
from lab2 import min_speed

class Test(unittest.TestCase):
    def test_func(self):
        self.assertEqual(min_speed([3,6,7,11], 8), 4)

    def test_func_2(self):
        self.assertEqual(min_speed([30,11,23,4,20], 5), 30)

    def test_func_3(self):
        self.assertEqual(min_speed([30,11,23,4,20], 6), 23)


if __name__ == '__main__':
    unittest.main()

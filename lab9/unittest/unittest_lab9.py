import unittest
import sys
import os

sys.path.append(r'C:\Users\Admin\Desktop\lab9\src')

from lab9 import longest_chain

class TestLongestChain(unittest.TestCase):
    def test_example(self):
        words = ["a", "b", "ba", "bca", "bda", "bdca"]
        self.assertEqual(longest_chain(words), 4)

if __name__ == "__main__":
    unittest.main()

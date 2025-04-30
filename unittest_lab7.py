import unittest
from lab7 import Trie, build

class TestTrie(unittest.TestCase):
    def setUp(self):
        patterns = ["apple", "app", "banana", "band", "bandana"]
        self.trie = build(patterns)

    def test_search_existing_words(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("banana"))
        self.assertTrue(self.trie.search("band"))
        self.assertTrue(self.trie.search("bandana"))

    def test_search_non_existing_words(self):
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("ban"))
        self.assertFalse(self.trie.search("banda"))
        self.assertFalse(self.trie.search("applepie"))

    def test_starts_with_true(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertTrue(self.trie.starts_with("band"))
        self.assertTrue(self.trie.starts_with("banda"))

    def test_starts_with_false(self):
        self.assertFalse(self.trie.starts_with("bat"))
        self.assertFalse(self.trie.starts_with("cat"))
        self.assertFalse(self.trie.starts_with("z"))

if __name__ == '__main__':
    unittest.main()

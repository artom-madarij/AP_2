class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def build(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

patterns = ["apple", "app", "banana", "band", "bandana"]
trie = build(patterns)

print(trie.search("apple"))   
print(trie.search("app"))     
print(trie.search("appl"))   
print(trie.starts_with("ban")) 
print(trie.starts_with("bat")) 

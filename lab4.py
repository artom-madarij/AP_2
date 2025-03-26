class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.height = 1
        self.left = None
        self.right = None


class AVLPriority:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node:
            return node.height
        else:
            return 0

    def _BF(self, node):
        if node:
            return self._height(node.left) - self._height(node.right)
        else:
            return 0

    def _rotate_right(self, y):
        x, y.left = y.left, y.left.right
        x.right, y.height = y, max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        y, x.right = x.right, x.right.left
        y.left, x.height = x, max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _balance(self, node):
        balance = self._BF(node)

        if balance > 1:
            if self._BF(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._BF(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)

        if priority > node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self._balance(node)

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _max(self, node):
        if not node.left:
            return node
        else:
            return self._max(node.left)

    def _delete_max(self, node):
        if not node.left:
            return node.right
        node.left = self._delete_max(node.left)
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self._balance(node)

    def pop(self):
        if not self.root:
            return None

        max_node = self._max(self.root)
        self.root = self._delete_max(self.root)
        return max_node.value

    def _inorder(self, node):
        if not node:
            return []
        return self._inorder(node.left) + [(node.value, node.priority)] + self._inorder(node.right)

    def view(self):
        return self._inorder(self.root)


if __name__ == "__main__":
    pq = AVLPriority()
    pq.insert("10", 3)
    pq.insert("30", 5)
    pq.insert("11", 2)
    pq.insert("20", 4)

    print(pq.view())

    print(pq.pop())

    print(pq.view())

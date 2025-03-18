class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

def invert_binary_tree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
    else:
        return
    
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

print('почакова')
in_order(root)

invert_binary_tree(root)

print('обернена')
in_order(root)
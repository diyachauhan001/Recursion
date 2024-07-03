class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaf_nodes(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.data, end=' ')
    print_leaf_nodes(node.left)
    print_leaf_nodes(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)

print("Leaf nodes of the BST are:")
print_leaf_nodes(root)

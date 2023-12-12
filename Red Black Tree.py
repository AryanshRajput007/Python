class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 represents red, 0 represents black


class RedBlackTree:
    def __init__(self):
        self.NULL_NODE = Node(None)
        self.NULL_NODE.color = 0  # Set color of NULL_NODE to black
        self.root = self.NULL_NODE

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.NULL_NODE
        node.right = self.NULL_NODE
        node.color = 1  # New node is always red

        y = None
        x = self.root

        while x != self.NULL_NODE:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0  # If the node is the root, color it black
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, node):
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # Uncle node
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right  # Uncle node

                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL_NODE:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL_NODE:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def inorder_traversal(self, node):
        if node != self.NULL_NODE:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)

    def search(self, node, key):
        if node == self.NULL_NODE or key == node.key:
            return node

        if key < node.key:
            return self.search(node.left, key)

        return self.search(node.right, key)


# Example usage:
tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)

print("Inorder Traversal:")
tree.inorder_traversal(tree.root)
print()

print("Search for key 30:")
result = tree.search(tree.root, 30)
if result != tree.NULL_NODE:
    print("Key 30 found!")
else:
    print("Key 30 not found!")
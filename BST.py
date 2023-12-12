import os

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.val = minValueNode(root.right).val
        root.right = delete(root.right, root.val)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)


if __name__ == "__main__":
  root = None
  while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nWhat do you want to do?")
    print("1. Insert a value")
    print("2. Delete a value")
    print("3. Search for a value")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to insert: "))
        root = insert(root, value)
        print("Inorder traversal of BST:")
        inorder_traversal(root)
    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        root = delete(root, value)
        print("Inorder traversal of BST:")
        inorder_traversal(root)
    elif choice == 3:
        value = int(input("Enter the value to search: "))
        result = search(root, value)
        if result:
            print("Value found in the BST")
        else:
            print("Value not found in the BST")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")

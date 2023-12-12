class tree:

  def __init__(self, key):
    self.val = key
    self.left = None
    self.right = None


def insert(root, key):
  if root is None:
    return tree(key)
  else:
    if key < root.val:
      root.left = insert(root.left, key)
    else:
      root.right = insert(root.right, key)
  return root


def inorder(root):
  if root is not None:
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


if __name__ == "__main__":
  root = None
  n = int(input())
  for i in range(n):
    data = int(input())
    root = insert(root, data)
  inorder(root)

class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def preorderTraversal(root):
  result = []
  stack = []
  current = root
  while True:
    while current:
      result.append(current.val)
      stack.append(current)
      current = current.left
    if not stack:
      break
    current = stack.pop()
    current = current.right
  return result


def preorderRecursive(root):
  result = []
  if root:
    result.append(root.val)
    result.extend(preorderRecursive(root.left))
    result.extend(preorderRecursive(root.right))
  return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

PreorderResultIterative = preorderTraversal(root)
print("Preorder Traversal (Iterative):", PreorderResultIterative)

PreorderResultRecursive = preorderRecursive(root)
print("Preorder Traversal (Recursive):", PreorderResultRecursive)

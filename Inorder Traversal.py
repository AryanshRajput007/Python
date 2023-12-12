class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def inorderTraversal(root):
  result = []
  stack = []
  current = root
  while True:
    while current:
      stack.append(current)
      current = current.left
    if not stack:
      break
    current = stack.pop()
    result.append(current.val)
    current = current.right
  return result


def inorder(root):
  result = []
  if root:
    result.extend(inorder(root.left))
    result.append(root.val)
    result.extend(inorder(root.right))
  return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inorderResult = inorderTraversal(root)
print("Inorder Traversal (Iterative):", inorderResult)

inorderRecursiveResult = inorder(root)
print("Inorder Traversal (Recursive):", inorderRecursiveResult)

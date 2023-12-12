class TreeNode:

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def PostOrderTraversalIterative(root):
  result = []
  stack = []
  current = root
  previous = None
  while True:
    while current is not None:
      stack.append(current)
      current = current.left
    if not stack:
      break
    while current is None and stack:
      current = stack[-1]
      if current.right is None or current.right is previous:
        result.append(current.val)
        stack.pop()
        previous = current
        current = None
      else:
        current = current.right
  return result


def PostOrderTraversalRecursive(root):
  result = []
  if root:
    result.extend(PostOrderTraversalRecursive(root.left))
    result.extend(PostOrderTraversalRecursive(root.right))
    result.append(root.val)
  return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

PostOrderResultIterative = PostOrderTraversalIterative(root)
print("Postorder Traversal (Iterative):", PostOrderResultIterative)

PostOrderResultRecursive = PostOrderTraversalRecursive(root)
print("Postorder Traversal (Recursive):", PostOrderResultRecursive)

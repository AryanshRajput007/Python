class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def append(self, data):
      new_node = Node(data)
      if not self.head:
          self.head = new_node
      else:
          last_node = self.head
          while last_node.next:
              last_node = last_node.next
          last_node.next = new_node

  def print_list(self):
      current_node = self.head
      while current_node:
          print(current_node.data)
          current_node = current_node.next

  def length(self):
      current_node = self.head
      count = 0
      while current_node:
          count += 1
          current_node = current_node.next
      return count

# Example usage
my_list = LinkedList()
my_list.append(2)
my_list.append(4)
my_list.append(3)

list = LinkedList()
list.append(5)
list.append(6)
list.append(4)

a = 10
result = 0
power = 0
current_node = my_list.head
while current_node:
  result += current_node.data * pow(a, power)
  power += 1
  current_node = current_node.next

print(result)

result2 = 0
power = 0
current_node = list.head
while current_node:
result2 += current_node.data * pow(a, power)
power += 1
current_node = current_node.next

print(result2)

result3 = int(str(result + result2)[::-1])

list3 = LinkedList()
for i in range(len(str(result3))):
list3.append(int(str(result3)[i]))

list3.print_list()

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
  def addTwoNumbers(self, l1, l2):

      :type l1: ListNode
      :type l2: ListNode
      :rtype: ListNode

      carry = 0
      dummy = ListNode(0)
      current = dummy

      while l1 or l2 or carry:
          val1 = l1.val if l1 else 0
          val2 = l2.val if l2 else 0
          carry, out = divmod(val1 + val2 + carry, 10)
          current.next = ListNode(out)
          current = current.next
          l1 = l1.next if l1 else None
          l2 = l2.next if l2 else None

      return dummy.next
"""

"""

501

class Solution(object):
def findMode(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    self.inorder_traversal(root, result)
    count_dict = {}

    for num in result:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    max_count = max(count_dict.values())
    most_common_elements = [num for num, count in count_dict.items() if count == max_count]
    return most_common_elements

def inorder_traversal(self, root, result):
    if root:
        self.inorder_traversal(root.left, result)
        result.append(root.val)
        self.inorder_traversal(root.right, result)


"""

"""

2265

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def averageOfSubtree(self, root):
      """
      :type root: Optional[TreeNode]
      :rtype: int
      """
      avg = inorder_traversal(root)/count_nodes(root)
      result = []
      self.inorder_traversal_list(root, result)
      n = 0
      for i in range(result):
          if(result[i] == avg):
              n += 1

  def inorder_traversal_list(self, root, result):
      if root:
          self.inorder_traversal_list(root.left, result)
          result.append(root.val)
          self.inorder_traversal_list(root.right, result)


def inorder_traversal(root):
  if root:
      result = 0
      inorder_traversal(root.left)
      result += root.val
      inorder_traversal(root.right)
      return result

def count_nodes(root):
  if root is None:
      return 0
  return 1 + count_nodes(root.left) + count_nodes(root.right)

  """
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

  def merge_list(self, ll2):
    current1 = self.head
    current2 = ll2.head
    list1 = []
    while current1:
      list1.append(current1.data)
      current1 = current1.next
    while current2:
      list1.append(current2.data)
      current2 = current2.next
    list1.sort()
    Merged_Sorted_list = LinkedList()
    while list1:
      Merged_Sorted_list.append(list1.pop(0))
    return Merged_Sorted_list


# Example usage
my_list = LinkedList()
my_list.append(2)
my_list.append(4)
my_list.append(3)

list = LinkedList()
list.append(5)
list.append(6)
list.append(4)

Merged_Sorted_List = my_list.merge_list(list)
Merged_Sorted_List.print_list()
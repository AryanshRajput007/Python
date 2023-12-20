class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


list_input = [
  int(x) for x in input("Enter the values separated by space: ").split()
]
hash_table = [None] * 10

for value in list_input:
  hash_key = value % 10
  if hash_table[hash_key] is None:
    hash_table[hash_key] = Node(value)
  else:
    temp = hash_table[hash_key]
    while temp.next is not None:
      temp = temp.next
    temp.next = Node(value)

for i in range(len(hash_table)):
  if hash_table[i] is not None:
    temp = hash_table[i]
    print(f"hash_table[{i}]:", end=" ")
    while temp is not None:
      print(temp.value, end=" -> ")
      temp = temp.next
    print("None")
  else:
    print(f"hash_table[{i}]: None")

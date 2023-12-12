class Node:

  def __init__(self, data):
    self.data = data


def createnode(data):
  newnode = Node(data)
  return newnode


def printarray(treearray, n):
  print("Array Representation of Binary Tree: ")
  for i in range(n):
    if treearray[i].data != -1:
      print(treearray[i].data, end=" ")
    else:
      print("-", end=" ")


Max_Nodes = 10
treearray = [None] * Max_Nodes

# Initialization of Array
for i in range(Max_Nodes):
  treearray[i] = createnode(-1)

treearray[0] = createnode(1)
treearray[1] = createnode(2)
treearray[2] = createnode(3)
treearray[3] = createnode(4)
treearray[4] = createnode(5)

printarray(treearray, Max_Nodes)

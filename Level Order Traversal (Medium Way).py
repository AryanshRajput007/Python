class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def initialization(arr, n):
    for i in range(n):
        arr[i] = -1

def Insertinarray(arr, n, data, index):
    if index < n:
        arr[index] = data

def display(arr, n):
    print("Binary Tree: ", end="")
    for i in range(n):
        if arr[i] != -1:
            print(arr[i], end=" ")
    print()

binarytree = [0] * 100
size = 0
initialization(binarytree, 100)
Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(-1)
Root.right.left = Node(5)
Insertinarray(binarytree, 100, Root.data, size)
size += 1
Insertinarray(binarytree, 100, Root.left.data, size)
size += 1
Insertinarray(binarytree, 100, Root.right.data, size)
size += 1
Insertinarray(binarytree, 100, Root.left.left.data, size)
size += 1
Insertinarray(binarytree, 100, Root.left.right.data, size)
size += 1
Insertinarray(binarytree, 100, Root.right.left.data, size)
size += 1
display(binarytree, size)
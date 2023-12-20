lst = [10, 12, 6, 5, 15, 20]
result = [-1] * len(lst)
stack = []

for i in range(len(lst)):
    while stack and lst[i] > lst[stack[-1]]:
        index = stack.pop()
        result[index] = lst[i]
    stack.append(i)

print(result)

"""
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stk = new Stack<Integer>();
        int ar1[] = {13, 7, 6, 12};
        int ar2[] = new int[4];
        int j = 3;
        for (int i = ar1.length - 1; i >= 0; i--) {
            if (stk.isEmpty()) {
                ar2[j--] = -1;
                stk.push(ar1[i]);
            } else if (ar1[i] < stk.peek()) {
                ar2[j--] = stk.peek();
                stk.push(ar1[i]);
            } else {
                while (!stk.isEmpty() && ar1[i] > stk.peek()) {
                    stk.pop();
                }
                if (stk.isEmpty()) {
                    ar2[j--] = -1;
                } else {
                    ar2[j--] = stk.peek();
                }
                stk.push(ar1[i]);
            }
        }
        for (int i = 0; i < 4; i++) {
            System.out.println(ar2[i]);
        }
    }
}
"""

"""
class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

def insertatbegin(head,data):
  newnode = Node(data)
  newnode.next = head
  return newnode

def printlist(head):
  current = head
  while(current != None):
    print(current.val,end=" ")
    current = current.next
  print()

def nextgreaterinteger(head):
  stack = []
  current = head
  while current:
    while stack and stack[-1].val < current.val:
      stack[-1].val = current.val
      stack.pop()
    stack.append(current)
    current = current.next
  while stack:
    stack.pop().val = -1
  printlist(head)

head = None
head = insertatbegin(head, 12)
head = insertatbegin(head, 5)
head = insertatbegin(head, 6)
head = insertatbegin(head, 13)
printlist(head)
nextgreaterinteger(head)
"""
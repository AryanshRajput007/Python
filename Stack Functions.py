class Stack:

  def __init__(self):
    self.stack = []

  def append(self, item):
    self.stack.append(item)

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    else:
      return "Stack is empty."

  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      return "Stack is empty."

  def is_empty(self):
    return len(self.stack) == 0


# Example usage:
my_stack = Stack()

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)

print(my_stack.peek())  # Output: 3

print(my_stack.pop())  # Output: 3
print(my_stack.pop())  # Output: 2
print(my_stack.pop())  # Output: 1
print(my_stack.pop())  # Output: Stack is empty.

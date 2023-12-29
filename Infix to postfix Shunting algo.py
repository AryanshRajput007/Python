def precedence(operator):
  if operator == '+' or operator == '-':
    return 1
  elif operator == '*' or operator == '/':
    return 2
  elif operator == '^':
    return 3
  else:
    return 0


def infix_to_Postfix_evaluation(infix):
  stack = []
  queue = []
  i = 0
  while i < len(infix):
    if infix[i] in ['+', '-', '*', '/', '^']:
      if len(stack) == 0:
        stack.append(infix[i])
      else:
        if precedence(stack[-1]) < precedence(infix[i]):
          stack.append(infix[i])
        else:
          while len(stack) != 0 and precedence(stack[-1]) >= precedence(
              infix[i]):
            queue.append(stack.pop())
          stack.append(infix[i])
    elif infix[i] == '(':
      stack.append(infix[i])
    elif infix[i] == ')':
      while stack[-1] != '(':
        queue.append(stack.pop())
      stack.pop()
    else:
      queue.append(infix[i])
    i += 1
  while len(stack) != 0:
    queue.append(stack.pop())
  postfix = ""
  while queue:
    postfix += queue.pop()
    postfix += " "
  return postfix[::-1]

infix = "a+b"
print(infix_to_Postfix_evaluation(infix))

def precedence(operator):
  if operator == '+' or operator == '-':
    return 1
  elif operator == '*' or operator == '/':
    return 2
  elif operator == '^':
    return 3
  else:
    return 0


def infix_to_postfix(infix):
  stack = []
  postfix = ""
  for char in infix:
    if char.isalnum():
      postfix += char
    elif char == "(":
      stack.append(char)
    elif char == ")":
      while stack and stack[-1] != "(":
        postfix += stack.pop()
      stack.pop()
    else:
      while stack and precedence(char) <= precedence(stack[-1]):
        postfix += stack.pop()
      stack.append(char)
  while stack:
    postfix += stack.pop()
  return postfix


def postfix_evaulation(postfix):
  postfix = postfix.replace('(', '').replace(')', '')
  stack = []
  for char in postfix:
    if char.isdigit():
      stack.append(int(char))
    else:
      num2 = stack.pop()
      num1 = stack.pop()
      if char == '+':
        stack.append(num1 + num2)
      elif char == '-':
        stack.append(num1 - num2)
      elif char == '*':
        stack.append(num1 * num2)
      elif char == '/':
        stack.append(num1 / num2)  # Use float division
      elif char == '^':
        stack.append(num1**num2)
      else:
        print(char)
        exit()
  return stack.pop()


infix_expression = str(input("Enter an infix expression: "))
infix_expression = infix_expression.replace(" ", "")
print("Infix_expression : " + infix_expression)
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix_expression : " + postfix_expression)
print("Result : " + str(postfix_evaulation(postfix_expression)))

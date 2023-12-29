#Test case :- ((10 + 5) * (8 - 3)) / (6 + 2)
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
  i = 0
  while i < len(infix):
    if infix[i].isdigit():
      num = ""
      while i < len(infix) and infix[i].isdigit():
        num += infix[i]
        i += 1
      postfix += num
      postfix += " "
      i -= 1  # Move back one position to account for the increment in the loop
    elif infix[i] == "(":
      stack.append(infix[i])
    elif infix[i] == ")":
      while stack and stack[-1] != "(":
        postfix += stack.pop()
        postfix += " "
      stack.pop()  # Discard the opening parenthesis
    else:
      while stack and precedence(infix[i]) <= precedence(stack[-1]):
        postfix += stack.pop()
        postfix += " "
      stack.append(infix[i])
    i += 1
  while stack:
    postfix += stack.pop()
    postfix += " "
  return postfix


def postfix_evaluation(postfix):
  stack = []
  postfix = postfix.split()  # Split the postfix expression into tokens
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


infix_expression = input("Enter an infix expression: ")
infix_expression = infix_expression.replace(" ", "")
print("Infix_expression : " + infix_expression)
postfix_expression = infix_to_postfix(infix_expression)
print("Postfix_expression : " + postfix_expression)
print("Result : " + str(postfix_evaluation(postfix_expression)))

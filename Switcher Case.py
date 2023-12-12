def add(a, b):
  c = a + b
  print(c)


def sub(a, b):
  c = a - b
  print(c)


def mult(a, b):
  c = a * b
  print(c)


def div(a, b):
  c = a / b
  print(c)


def fact(a, b):
  result = 1
  for i in range(1, a + 1):
    result *= i
  print(result)


def switcher(choice):
  switcher = {1: add, 2: sub, 3: mult, 4: div, 5: fact}
  func = switcher.get(choice)
  if func == add or func == sub or func == mult or func == div:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    func(a, b)
  elif func == fact:
    a = int(input("Enter the number: "))
    b = None
    func(a, b)
  else:
    print("Invalid choice")


# The main function starts from here
choice = int(input("Enter your choice: "))

switcher(choice)

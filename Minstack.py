import os


def clear_screen():
  # Clear the screen for Windows
  if os.name == 'nt':
    _ = os.system('cls')
    # Clear the screen for Unix/Linux/MacOS
  else:
    _ = os.system('clear')


Stack = []
Minstack = []

while True:
  clear_screen()

  print("Select what operation you want to perform:")
  choice = int(
    input(
      "Press 1 to Push\nPress 2 to Pop\nPress 3 to Display\nPress 4 to Display the Minstack\nPress 5 to exit\nEnter your choice: "
    ))

  if choice == 1:
    num = int(input("Enter a value: "))
    Stack.append(num)
    if len(Minstack) == 0:
      Minstack.append(num)
    if num < Minstack[-1]:
      Minstack.append(num)
  elif choice == 2:
    if len(Stack) == 0:
      print("Stack is empty")
    if Stack[-1] < Minstack[-1]:
      Minstack.pop()
    Stack.pop()
  elif choice == 3:
    print(Stack)
  elif choice == 4:
    print(Minstack)
  elif choice == 5:
    exit()
  else:
    print("Invalid choice")
  input("Press Enter to continue...")

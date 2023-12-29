import os

while True:
  my_list = [
    int(x)
    for x in input("Enter a list of numbers separated by commas: ").split(",")
  ]
  average_of_a_list = sum(my_list) / len(my_list)
  print(average_of_a_list)

  input("Press Enter to continue...")
  os.system(
    'cls' if os.name == 'nt' else 'clear')  # Clear screen based on the OS

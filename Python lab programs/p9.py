import os

while True:
  nums = int(input("Enter a number for which you want to get the table: "))
  for i in range(1, 11):
    print(nums, "*", i, "=", nums * i)

  input("Press Enter to continue...")
  os.system('cls' if os.name == 'nt' else 'clear')
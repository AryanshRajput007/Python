import os

while True:
  nums = int(input("Enter a decimal number whose base conversion you want: "))
  Binary = bin(nums)
  Hexadecimal = hex(nums)
  Octal = oct(nums)
  print(f"Binary: {Binary} \nOctal: {Octal} \nHexadecimal: {Hexadecimal}")

  input("Press Enter to continue...")
  os.system('cls' if os.name == 'nt' else 'clear')

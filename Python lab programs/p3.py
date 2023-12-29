import os
import random
import string

while True:
  all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
  length = int(input("Enter the length of the password: "))
  password = "".join(random.sample(all_chars, length))
  print(password)

  input("Press Enter to continue...")
  os.system('cls' if os.name == 'nt' else 'clear')

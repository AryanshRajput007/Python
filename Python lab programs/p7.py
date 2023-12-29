def is_palindrome(s):
  s = s.lower()
  return s == s[::-1]

s = str(input("Enter the value: "))
if is_palindrome(s):
  print("The string is palindrome")
else:
  print("The string is not palindrome")
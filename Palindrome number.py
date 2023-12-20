def ispalindrome(nums):
  palindrome = str(nums)
  if nums >= 0:
    return (palindrome) == (palindrome[::-1])
  elif nums < 0:
    return (palindrome) == (palindrome[::-1])
  else:
    print('error')

num = int(input("Enter a number: "))
print("Is the number, palindrome: ", ispalindrome(num))
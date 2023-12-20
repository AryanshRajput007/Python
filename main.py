def converter(nums):
  a = int(nums)
  b = float(nums)
  c = str(nums)
  d = bool(nums)
  e = complex(nums)
  print(a)
  print(type(a))
  print(b)
  print(type(b))
  print(c)
  print(type(c))
  print(d)
  print(type(d))
  print(e)
  print(type(e))
  
converter(input("Enter a number: "))
nums = complex(input("Enter a number: "))
num = bool(input("Enter a number: "))
print(num)

a = 10
b = 10
c = 10
print(a is b is c)
print(id(a), id(b), id(c))
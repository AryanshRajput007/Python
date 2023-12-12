num1 = [1, 2]
num2 = [3, 4]

len1 = len(num1)
len2 = len(num2)
len = len1 + len2
Median = 0

if (len % 2 != 0):
  Median = (len + 1) // 2
  num = num1 + num2
  num.sort()
  print(float(num[Median - 1]))
elif (len % 2 == 0):
  Median = (len) // 2
  num = num1 + num2
  num.sort()
  print((num[Median - 1] + num[Median]) / 2)
else:
  print("Error")

# list = [2, 7, 11, 15]
# Target = int(input("Enter the target value: "))

# for i in range(0, len(list)):
#     for j in range(1, len(list)):
#         if Target == list[i] + list[j]:
#             result = [i, j]
#             print(result)

arr = [5, 7, 7, 8, 8, 10]
Target1 = int(input("Enter the Target value : "))
res = []
a = 0
for i in range(0, len(arr)):
  if (arr[i] is Target1):
    res.append(i)
    a += 1
if (a == 0):
  res = [-1, -1]
print(res)

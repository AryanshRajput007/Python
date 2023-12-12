list = [100, 90, 80, 60, 50]

for i in range(0, len(list)):
  for j in range(i + 1, len(list)):
    if (list[i] > list[j]):
      temp = list[i]
      list[i] = list[j]
      list[j] = temp

print(list)

#9589832255 Rahul Sharama

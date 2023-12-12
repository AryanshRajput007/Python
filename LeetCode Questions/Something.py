def repeat_remover(my_list):
  my_list.sort()
  list2 = []
  for i in range(len(my_list)):
    if i == 0 or my_list[i - 1] != my_list[i]:
      list2.append(my_list[i])
  counter(my_list, list2)


def counter(my_list, list2):
  count = {}
  for i in range(len(list2)):
    counter = 0
    for j in range(len(my_list)):
      if my_list[j] == list2[i]:
        counter += 1
    count[list2[i]] = counter
  print(count)
  max_count = max(count.values())
  for key, value in count.items():
    if value == max_count:
      print("The element with the maximum count is:", key)


my_list = [1, 2, 2, 6, 6, 6, 6, 7, 10]
repeat_remover(my_list)

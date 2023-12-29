# list = [1,2,3,1,1,1,7,8,1]
# list.remove(3)
# print(list)
# # for i in range(len(list)):
# #   if list[i] == 1:
# #     list[i] = 10
# # print(list)
# for i in range(len(list) // 2):
#   if list [i] == 1:
#     list[i] = 10
#   if list[len(list) - i - 1] == 1:
#     list[len(list) - i - 1] = 10
# print(list)

# n = "shark"
# x = [x for x in n]
# print(x)
# s = "abcabcbb"
# list = []
# for i in range(len(s)):
#   if s[i] not in list:
#     list.append(s[i])
# result = len(list)

# list = [int(x) for x in input().split()]
# list = [10 if x == 1 else(20 if x == 2 else x)  for x in list]
# print(list)

# for i in range(len(list) // 2):
#   if list [i] == 1:
#     list[i] = 10
#   if list[len(list) - i - 1] == 1:
#     list[len(list) - i - 1] = 10

# list = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#   list.append(int(input("Enter the element: ")))
#   if list[i] == 1:
#     list[i] = 10
#   if list[i] == 2:
#     list[i] = 20
# print(list)

# def func():
#   list = []
#   n = int(input("Enter the number of elements: "))
#   for i in range(n):
#     list.append(int(input("Enter the element: ")))
#     list [i] = (list[i] % 10) * 10
#   return list

# print(func())

# n = 5
# list = [x for x in range(n)]
# print(list)

# list = [int(x) for x in input("Enter the values seperated by spaces: ").split()]
# list2 = [x for x in list if x % 2 == 0]
# print("The even list is: ",list2)
# list3 = [x for x in list if x % 2 != 0]
# print("The odd list is: ", list3)

t = (10, 20, 30, 40)
t = t + (300,)  
t = t[:t.index(10)] + t[t.index(10)+1:]
print(t)
print(id(t))
print(type(t))
t2 = (10,)
print(t2[0])

words = ("apple", "banana", "cherry")
for index, word in enumerate(words, start = 1):
    print(f"Word {index}: {word}")

my_set = [3, 1, 2, 3, 4, 5, 1, 2]
print(set(my_set))
list1 = [1, 2, 2, 3]
list2 = ["abc", "xyz", "abc", "rzy"]
map = {}

for i in range(len(list1)):
  if list1[i] not in map:
    map[list1[i]] = []
  map[list1[i]].append(list2[i])
print(map)

s = set({})
print(type(s))

set1 = {15,20,25}
set2 = {30,40,50}
set1.add(10)
if 0 in set1:
    set1.remove(0)
print(set1.union(set2))
print(set1)
print(set1.intersection(set2))

set3 = {"Nanimo", "Bankai", "Gotei", 13, ("Ichigo", "Ken", "Saitama")}
print(set3)
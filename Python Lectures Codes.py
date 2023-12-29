# def converter(nums):
#   a = int(nums)
#   b = float(nums)
#   c = str(nums)
#   d = bool(nums)
#   e = complex(nums)
#   print(a)
#   print(type(a))
#   print(b)
#   print(type(b))
#   print(c)
#   print(type(c))
#   print(d)
#   print(type(d))
#   print(e)
#   print(type(e))

# converter(input("Enter a number: "))
# nums = complex(input("Enter a number: "))
# num = bool(input("Enter a number: "))
# print(num)

# a = 10
# print(id(a))
# a = a + 10
# print(a)
# print(id(a))
# b = 10
# c = 10
# print(a is b is c)
# print(id(a), id(b), id(c))

x = 'ab', 'cd', 'ef'
print(x)
print(type(x))

my_list = [int(x) for x in input("Enter the values separated by space: ").split(" ")]
print(my_list)

from array import array
# lst = [int(x) for x in input("Enter the value separated by space: ").split()]
my_list = [10, 20, 30, 40, 50]
my_list.insert(3, 70)
print(type(my_list))
print(my_list)
print(max(my_list))
print(my_list.count(50))
print(min(my_list))
print(my_list.index(30))
my_list.remove(70)
print(my_list)
print(my_list[::-1])
my_list.reverse()
print(my_list)
print(id(my_list))
sorted_list = sorted(my_list)
print(sorted_list)

new_list = ure
# for i in range(len(new_list)):
#     if isinstance(new_list[i], list):
#         for j in range(len(new_list[i])):
#             print(new_list[i][j])
#     elif isinstance(new_list[i], set):
#         print(', '.join(new_list[i]))
#     else:
#         print(new_list[i])

arr = array('i', [1,2,3,4,5])
print(arr)

lst = [10, 20, 30, 40]
lst[1] = 70
print(lst)
lst2 = lst
lst2.extend(my_list)
print(id(lst))
print(id(lst2))
print(lst2)
print(lst)
print(lst[1:4])

for i in range(len(lst)):
  print(lst[i:])

for i in range(len(lst)):
  print(lst[:i])

import math

# Taking input for list1
list1 = [
  int(x)
  for x in input("Enter the elements of list1 separated by space: ").split()
]

# Taking input for list2
list2 = [
  int(x)
  for x in input("Enter the elements of list2 separated by space: ").split()
]
n = len(list1)

print("Enter 1 for Base Formula Method")
print("Enter 2 for Modified Formula Method")
print("Enter 3 for Spearman's Formula if rank is given")
print(
  "Enter 4 for Spearman's Formula if the rank is not given and no repetition")

choice = int(input("Your Choice: "))

if choice == 1:
  mean_of_x = sum(list1) / n
  mean_of_y = sum(list2) / n

  print("The mean of X :" + str(mean_of_x))
  print("The mean of Y :" + str(mean_of_y))

  mean_sum_list_of_x = [x - mean_of_x for x in list1]
  print("The list after x - mean of x : " + str(mean_sum_list_of_x))

  mean_sum_list_of_y = [y - mean_of_y for y in list2]
  print("The list after y - mean of y : " + str(mean_sum_list_of_y))

  mean_sum_square_list_of_x = [x**2 for x in mean_sum_list_of_x]
  mean_sum_square_list_of_y = [y**2 for y in mean_sum_list_of_y]
  print("The list after x\u00B2 :" + str(mean_sum_square_list_of_x))
  print("The list after y\u00B2 :" + str(mean_sum_square_list_of_y))

  sum_of_mean_square_list_of_x = sum(mean_sum_square_list_of_x)
  sum_of_mean_square_list_of_y = sum(mean_sum_square_list_of_y)
  print("The sumation of x\u00B2 :" + str(sum_of_mean_square_list_of_x))
  print("The sumation of y\u00B2 :" + str(sum_of_mean_square_list_of_y))

  mul_of_sum_of_list_xy = [
    x * y for x, y in zip(mean_sum_list_of_x, mean_sum_list_of_y)
  ]
  print("The list of (x - mean of x)(y - mean of y) :" +
        str(mul_of_sum_of_list_xy))

  sum_of_mul_of_sum_list_xy = sum(mul_of_sum_of_list_xy)
  print("The sum of list of (x - mean of x)(y - mean of y) : " +
        str(sum_of_mul_of_sum_list_xy))

  r = sum_of_mul_of_sum_list_xy / (math.sqrt(
    sum_of_mean_square_list_of_x * sum_of_mean_square_list_of_y))
  print("The Coefficient of Correltion : " + str(r))

if choice == 2:
  if n > 0:
    sum_of_x = sum(list1)
    sum_of_y = sum(list2)
    sum_of_x_squared = sum(x**2 for x in list1)
    sum_of_y_squared = sum(y**2 for y in list2)
    sum_of_xy = sum(x * y for x, y in zip(list1, list2))
    temp = [list1 * list2 for i in range(n)]
    square_of_x = [x**2 for x in list1]
    square_of_y = [y**2 for y in list2]
    a = (n * sum_of_xy - sum_of_x * sum_of_y)
    c = (n * sum_of_x_squared - sum_of_x**2)
    d = (n * sum_of_y_squared - sum_of_y**2)

    r = a / (math.sqrt(c * d))
    print("The sumation of x :" + str(sum_of_x))
    print("The sumation of y :" + str(sum_of_y))
    print("The list xy :" + str(temp))
    print("The sumation of xy :" + str(sum_of_xy))
    print("The list x\u00B2 :" + str(square_of_x))
    print("The sumation of x\u00B2 :" + str(sum_of_x_squared))
    print("The list y\u00B2 :" + str(square_of_y))
    print("The sumation of y\u00B2 :" + str(sum_of_y_squared))
    print("The Coefficient of Correlation :" + str(r))
  else:
    print("Lists are empty")
else:
  print("Invalid Choice")

if choice == 3:
  d = [list1[i] - list2[i] for i in range(n)]
  print("The list of D :" + str(d))
  sum_of_d = sum(d)
  print("The sumation of D :" + str(sum_of_d))
  sd = [d[i]**2 for i in range(n)]
  print("The List of x\u00B2 : " + str(sd))
  sum_of_d_squared = sum(x**2 for x in d)
  print("The sumation of x\u00B2 :" + str(sum_of_d_squared))
  r = 1 - ((6 * sum_of_d) / (n * math.sqrt(n**2 - 1)))
  print("The coefficient of correlation :" + str(r))

if choice == 4:
  temp_list1 = []
  index_list = []
  temp_list1 = [list1[i] for i in range(n)]
  temp_list1.sort()
  for i in range(n):
    a = 1
    for j in range(n):
      if temp_list1[i] == list1[j]:
        index_list.append(n - a + 1)
      else:
        a += 1
  print(index_list)
  temp_list2 = []
  index_list2 = []
  temp_list2 = [list2[i] for i in range(n)]
  temp_list2.sort()
  for i in range(n):
    a = 1
    for j in range(n):
      if temp_list2[i] == list2[j]:
        index_list2.append(n - a + 1)
      else:
        a += 1

  print(index_list2)

  d = [index_list[i] - index_list2[i] for i in range(n)]
  print(d)
  sum_of_d = sum(d)
  print(sum_of_d)
  square_of_d = [d[i]**2 for i in range(n)]
  print(square_of_d)
  sum_of_square_of_d = sum(square_of_d)
  print(sum_of_square_of_d)
  print(n)
  r = 1 - ((6 * sum_of_square_of_d) / (n * (n**2 - 1)))
  print(r)
"""
Enter the elements of list1 separated by space: 10 14 18 22 26 30 10
Enter the elements of list2 separated by space: 18 12 24 6 30 36 18
Enter 1 for Base Formula Method
Enter 2 for Modified Formula Method
Enter 3 for Spearman's Formula if rank is given
Enter 4 for Spearman's Formula if the rank is not given and no repetition
Your Choice: 2
The sumation of x :130
The sumation of y :144
The list xy :[180, 168, 432, 132, 780, 1080, 180]
The sumation of xy :2952
The list x² :[100, 196, 324, 484, 676, 900, 100]
The sumation of x² :2780
The list y² :[324, 144, 576, 36, 900, 1296, 324]
The sumation of y² :3600
The Coefficient of Correlation :0.5750613571751532
"""
"""
# def count_occurrences(lst, target_number):
#   return lst.count(target_number)

# def remove_duplicates(sorted_list):
#   unique_list = []
#   previous_element = None

#   for element in sorted_list:
#     if element != previous_element:
#       unique_list.append(element)
#       previous_element = element

#   return unique_list

# list1 = [35, 40, 42, 43, 40, 53, 54, 49, 41, 55]
# list2 = [102, 101, 97, 989, 38, 101, 97, 92, 95, 95]

# if len(list1) == len(list2):
#   n = len(list1)
#   # Initialize lists before the loop
#   occurrences_of_l1 = []
#   occurrences_of_l2 = []

#   # Example usage:
#   for i in range(n):
#       occurrences_of_l1.append(count_occurrences(list1, list1[i]))

#   for i in range(n):
#       occurrences_of_l2.append(count_occurrences(list2, list2[i]))

#   print(occurrences_of_l1)
#   print(occurrences_of_l2)

#   repeating_numbers_in_list1 = []
#   repeating_numbers_in_list2 = []

#   for i in range(n):
#     if occurrences_of_l1[i] > 1:
#       repeating_numbers_in_list1.append(list1[i])

#   for i in range(n):
#     if occurrences_of_l2[i] > 1:
#       repeating_numbers_in_list2.append(list2[i])

#   repeating_numbers_in_list1.sort()
#   repeating_numbers_in_list2.sort()

#   print(repeating_numbers_in_list1)
#   print(repeating_numbers_in_list2)

#   unique_repeating_numbers_in_list1 = remove_duplicates(repeating_numbers_in_list1)
#   unique_repeating_numbers_in_list2 = remove_duplicates(repeating_numbers_in_list2)

#   print(unique_repeating_numbers_in_list1)
#   print(unique_repeating_numbers_in_list2)

#   repeating_numbers_index_in_list1 = []
#   repeating_numbers_index_in_list2 = []
#   unique_temp_list1 = remove_duplicates(list1)
#   unique_temp_list2 = remove_duplicates(list2)

#   for i in range(n):
#     for j in range(len(unique_repeating_numbers_in_list1)):
#       if list1[i] == unique_repeating_numbers_in_list1[j]:
#         repeating_numbers_index_in_list1.append(i + 1)

#   for i in range(n):
#     for j in range(len(unique_repeating_numbers_in_list2)):
#       if list2[i] == unique_repeating_numbers_in_list2[j]:
#         repeating_numbers_index_in_list2.append(i + 1)

#   print(repeating_numbers_index_in_list1)
#   print(repeating_numbers_index_in_list2)


# else:
#   print("Lists are not of the same length.")

list1 = [35, 40, 42, 43, 40, 53, 54, 49, 41, 55]
list2 = [102, 101, 97, 98, 38, 101, 97, 92, 95, 95]

# Check if the lengths of both lists are equal
if len(list1) == len(list2):
    # Sort the lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    # Print the sorted lists
    print("Sorted List 1:", sorted_list1)
    print("Sorted List 2:", sorted_list2)

    # Find repeating elements in each list
    repeating_numbers_in_list1 = [x for x in sorted_list1 if sorted_list1.count(x) > 1]
    repeating_numbers_in_list2 = [x for x in sorted_list2 if sorted_list2.count(x) > 1]

    # Print repeating elements
    print("Repeating Numbers in List 1:", repeating_numbers_in_list1)
    print("Repeating Numbers in List 2:", repeating_numbers_in_list2)

    # Find unique repeating elements in each list
    unique_repeating_element_list1 = []
    unique_repeating_element_list2 = []

    # Iterate over repeating elements in List 1
    previous_element = None
    for element in repeating_numbers_in_list1:
        if element != previous_element:
            unique_repeating_element_list1.append(element)
            previous_element = element

    # Iterate over repeating elements in List 2
    previous_element = None
    for element in repeating_numbers_in_list2:
        if element != previous_element:
            unique_repeating_element_list2.append(element)
            previous_element = element

    # Print unique repeating elements
    print("Unique Repeating Elements in List 1:", unique_repeating_element_list1)
    print("Unique Repeating Elements in List 2:", unique_repeating_element_list2)

    index_list1 = []
    index_list2 = []

    # Find indices of unique repeating elements in the sorted lists
    for i in range(len(sorted_list1)):
        for j in range(len(unique_repeating_element_list1)):
            if sorted_list1[i] == unique_repeating_element_list1[j]:
                index_list1.append(i)

    for i in range(len(sorted_list2)):
        for j in range(len(unique_repeating_element_list2)):
            if sorted_list2[i] == unique_repeating_element_list2[j]:
                index_list2.append(i)

    print("Indices of Unique Repeating Elements in List 1:", index_list1)
    print("Indices of Unique Repeating Elements in List 2:", index_list2)

    temp_list1 = []
    temp_list2 = []
    temp = None

    # Calculate the average of adjacent elements in index_list1
    for i in range(len(index_list1) - 1):
        temp = (index_list1[i] + index_list1[i + 1]) / 2
        temp_list1.append(temp)

    print("Average of Adjacent Indices in List 1:", temp_list1)

    # Calculate the average of adjacent elements in index_list2
    temp_list2 = []
    for i in range(0, len(index_list2) - 1, 2):  
      # Increment by 2 to consider pairs
      temp = (index_list2[i] + index_list2[i + 1]) / 2
      temp_list2.append(temp)
    print("Average of Adjacent Indices in List 2:", temp_list2)
    for i in range(len(list2)):
      pairs = []
      if i in index_list1:
        for j in range(0, len(index_list1), 2):
          pair = index_list1[i:i + 2]
          pairs.append(pair)
          if i in pairs:
            rank_of_pair = pairs.index(i) + 1

else:
    print("Lists are of different lengths.")
"""

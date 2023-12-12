def interpolationsearch(arr, size, x):
  low = 0
  high = size - 1
  while low <= high and x >= arr[low] and x <= arr[high]:
    if low == high:
      if arr[low] == x:
        return low
      else:
        return -1
    pos = int(low + (((high - low) / (arr[high] - arr[low])) * (x - arr[low])))
    #OR we can use the following formula
    #pos = low + (((high - low) // (arr[high] - arr[low])) * (x - arr[low]))

    if arr[pos] == x:
      return pos
    if x < arr[pos]:
      high = pos - 1
    else:
      low = pos + 1
  return -1


# Main
import array

arr = array.array('i')

n = int(input("Enter the number of elements in the array: "))

print("Enter the elements of the array:")
for _ in range(n):
  element = int(input())
  arr.append(element)

print("Array:", arr)

x = int(input("Enter the element you want to search: "))

size = len(arr)

index = interpolationsearch(arr, size, x)
if index != -1:
  print("The element " + str(x) + " is present at the index " + str(index))
else:
  print("The element " + str(x) + " is not found in the array")

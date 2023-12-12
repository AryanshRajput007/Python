def interpolation_search(arr, n, x):
  low = 0
  high = n - 1

  while low <= high and x >= arr[low] and x <= arr[high]:
    if low == high:
      if arr[low] == x:
        return low
      return -1

    pos = low + int(((high - low) / (arr[high] - arr[low])) * (x - arr[low]))

    if arr[pos] == x:
      return pos

    if arr[pos] < x:
      low = pos + 1
    else:
      high = pos - 1

  return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = len(arr)
x = 10
index = interpolation_search(arr, n, x)

if index != -1:
  print(f"Element {x} found at index {index}")
else:
  print(f"Element {x} not found in the array")

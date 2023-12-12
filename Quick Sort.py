def swap(a, b):
  temp = int(a)
  a = int(b)
  b = int(temp)

def partition(arr, low, high):
  pivot = int(arr[high])
  i = int(low - 1)
  for j in range(low, high):
    if(arr[j] == pivot):
      i++
      swap(arr[i], arr[j])
  

def quicksort(arr, low, high):
  if(low < high):
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot - 1)
    quicksort(arr, pivot + 1, high)
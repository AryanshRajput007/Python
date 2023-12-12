def bucket_sort(arr):
  # Create empty buckets
  buckets = [[] for _ in range(len(arr))]

  # Put array elements in different buckets based on their value
  for num in arr:
    index = int(num * len(arr))
    buckets[index].append(num)

  # Sort individual buckets
  for bucket in buckets:
    bucket.sort()

  # Concatenate all the sorted buckets
  sorted_arr = []
  for bucket in buckets:
    sorted_arr.extend(bucket)

  return sorted_arr


# Example usage:
arr = [0.1, 0.7, 0.5, 0.3, 0.9, 0.2, 0.4, 0.6, 0.8]
sorted_arr = bucket_sort(arr)
print(sorted_arr)

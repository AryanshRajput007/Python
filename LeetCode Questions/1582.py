def numSpecial(mat):
  m, n = len(mat), len(mat[0])
  row_count = [0] * m
  col_count = [0] * n
  special_positions = 0

  # Count the number of 1s in each row and each column
  for i in range(m):
      for j in range(n):
          if mat[i][j] == 1:
              row_count[i] += 1
              col_count[j] += 1
  print(str(row_count) + "" + str(col_count))
  # Check if the current position is special
  for i in range(m):
      for j in range(n):
          if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
              special_positions += 1

  return special_positions

# Example usage:
matrix = [
  [1, 0, 0],
  [0, 0, 1],
  [1, 0, 0]
]

result = numSpecial(matrix)
print(result)

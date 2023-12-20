def differenceMatrix(mat):
  m, n = len(mat), len(mat[0])

  # Count the number of ones in each row and each column
  ones_row = [0] * m
  ones_col = [0] * n

  for i in range(m):
      for j in range(n):
          if mat[i][j] == 1:
              ones_row[i] += 1
              ones_col[j] += 1

  # Create the difference matrix diff
  diff = [[0] * n for _ in range(m)]

  for i in range(m):
      for j in range(n):
          zeros_row = n - ones_row[i]
          zeros_col = m - ones_col[j]
          diff[i][j] = ones_row[i] + ones_col[j] - zeros_row - zeros_col

  return diff

# Example usage:
matrix = [[0,1,1],[1,0,1],[0,0,1]]

result_diff = differenceMatrix(matrix)
for row in result_diff:
  print(row)

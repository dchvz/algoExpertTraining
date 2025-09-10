# Transpose Matrix 🟢
# You're given a two-dimensional array (a matrix) of integers. Write a function that transposes the matrix.
# The transpose of a matrix is a new matrix whose rows are the columns of the original.
# For example, the transpose of the matrix:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# is:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]

# Time Complexity 0(n*m) where n and m are the columns and rows
# Space Complexity 0(m*n) where n and m are the columns and rows
def transpose_matrix(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  # created a transposed empty matrix because we can't transpose in place
  # this also allows us to handle non-square matrices
  transposed = [[0] * rows for _ in range(cols)]

  for i in range(rows):
    for j in range(cols):
      transposed[j][i] = matrix[i][j]

  return transposed

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
print(transpose_matrix([[1]]))

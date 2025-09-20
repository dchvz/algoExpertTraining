# Spiral Traverse 🔵
# Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m)
# and returns a one-dimensional array of all the array's elements in spiral order.
# Sample Input
# array = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
# ]
# Sample Output
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

# just traverse the perimeter
# Mark the starting end ending points and move them
# [     sc   ec
#     sr[1,2,3]
#       [4,5,6]
#     er[7,8,9]
# ]
# from row i to col j
# sr = 0, er = 2, sc = 0, ec = 2
# from sr(0) to ec: columns increase from 0 to n
# from sr to er, current col is static(ec), rows increase from 0 to n
# from er to sc, current row stays the same, cols decrease value
# from er to sr, current col is static, which is startCol, reverse the row values from n to 0
# sr += 1
# er -= 1
# sc += 1
# ec -= 1
# [            sc/ec
#            [1, 2, 3]
#     sr/er  [4, 5, 6]
#            [7, 8, 9]
# ]

# Time Complexity O(n)
# Space Complexity O(n)
def spiralTraverse(array):
  result = []
  startRow, endRow = 0, len(array) - 1
  startCol, endCol = 0, len(array[0]) - 1

  while startRow <= endRow and startCol <= endCol:
    print('startRow-endRow', startRow, endRow)
    print('startCol-endCol', startCol, endCol)
    for col in range(startCol, endCol + 1):
      print('right', array[startRow][col])
      result.append(array[startRow][col])

    for row in range(startRow + 1, endRow + 1):
      print('down', array[row][endCol])
      result.append(array[row][endCol])

    for col in reversed(range(startCol, endCol)):
      if (startRow == endRow):
        break
      print('left', array[endRow][col])
      result.append(array[endRow][col])

    for row in reversed(range(startRow + 1, endRow)):
      if (startCol == endCol):
        break
      print('up', array[row][startCol])
      result.append(array[row][startCol])

    startRow += 1
    endRow -= 1
    startCol += 1
    endCol -= 1

  return result;

print(spiralTraverse([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
])) # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralTraverse([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
])) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(spiralTraverse([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
])) # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

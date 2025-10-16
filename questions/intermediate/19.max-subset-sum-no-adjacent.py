# [7, 10, 12, 7, 9, 14]
# we will try to sum the current max sum on each iteration for non adjacent numbesr
# if index 0 then just return first element
# if index 1 just return second element
# otherwise, the result is the max between: the previous max or the last to prev max + current number
# [7, 10, 19(10 or 19), 19(17 or 19), 28(19 or 28), 33(28 or 33)]

# [75, 105, 120, 75, 90, 135]
# # 75, 105
# first 75
# second 105
# max = 120 + 75 = 195
# 75, 105, 195
# first = 105
# second = 195
# 195 or 105 + 75(180)
# 75, 105, 195, 195
# first = 195
# second = 195
# 195 or 90 + 195(285)
# 75, 105, 195, 195, 285,
# first = 195
# second = 285
# 285 or 135 + 195
# 330

# [4, 3, 5, 200, 5, 3]
# 4
# 3
# first = 4
# second = 3
# 4,3
# 5 + 4 or 3
# 4,3,9
# first = 3
# second = 9
# 200 + 3 or 9
# in this case I HAD TO GO ONE ELEMENT BEFORE!
# 4,3,9,203
# 10 or 203?
# 4,3,9,203

# Time Complexity O(n)
# Space Compelxity O(1)
def maxSubsetSumNoAdjacent(array):
  if len(array) == 0:
    return 0
  if len(array) == 1:
    return array[0]
  if len(array) == 2:
    return max(array[0],array[1])

  first = array[0]
  second = array[1]
  new_max = 0

  for i in range(2, len(array)):
    curr_max = first + array[i]
    new_max = max(second, curr_max)
    first = max(first, second)
    second = new_max

  return new_max
# Monotonic Array 🔵
# Write a function that takes in an array of integers and returns a boolean
# representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right,
# are entirely non-increasing or entirely non-decreasing.
# Non-increasing elements aren't necessarily exclusively decreasing;
# they simply don't increase. Similarly, non-decreasing elements aren't
# necessarily exclusively increasing; they simply don't decrease.
# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Sample Output
# true

# [-1, -5 , -10, -10, -11]
# since -5 <= -1, should be non-increasing!
# -10 <= -5, good
# -10 <= 10, good
# -11 <= 10, good
# in a different case:
# [-1, -5 , -10, -10, -11,1]
# 1 <= -11, no, so return False

# [1,4,6,8]
# 1 and 4
# 4 >= 1, so should be non-decreasing!
# 6 >= 4, yes, good
# 8 >= 6, yes, good

# Time Complexity O(n)
# Space Complexity O(1)
def is_monotonic(array):
  is_decreasing = True
  is_type_known = False
  for index in range(0, len(array) - 1):
    current = array[index]
    next = array[index + 1]
    if not is_type_known:
      if next != current:
        is_type_known = True
        if next > current:
          is_decreasing = False
    else:
      if is_decreasing and next > current:
        return False
      elif not is_decreasing and next < current:
        return False
  return True

print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001])) # True
print(is_monotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001, 0])) # False
print(is_monotonic([1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8, 9, 1])) # False
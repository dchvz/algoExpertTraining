# Smallest Difference 🔵
# Find the pair of numbers (one from each array) whose absolute difference is closest to zero
# and return an array containing these two numbers, with the number from the first array in the
# first position. If there are multiple pairs, return the pair with the smallest sum.
# Note that the absolute difference of two integers is the distance between them on the real
# number line. For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5
# and -4 is 1.
# You can assume that there will only be one pair of numbers with the smallest difference.
# Each input array will contain at least one integer.
# The input arrays are not guaranteed to be sorted.
# Sample Input
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
# Sample Output
# [28, 26] // The smallest difference is 2 (28 - 26)

# By sorting both arrays we can find the smallest difference by going all of them once
# Time Complexity O(nlogn + mlogm)
# Space Complexity O(1)
def smallest_difference(arrayOne, arrayTwo):
  arrayOne.sort()
  arrayTwo.sort()
  closest, pair = float('inf'), []
  first_index = 0
  second_index = 0
  while first_index < len(arrayOne) and second_index < len(arrayTwo):
    first, second = arrayOne[first_index], arrayTwo[second_index]
    diff = abs(first - second)
    if diff < closest:
      closest = diff
      pair = [first, second]
    if first < second:
      first_index += 1
    else:
      second_index += 1
  return pair

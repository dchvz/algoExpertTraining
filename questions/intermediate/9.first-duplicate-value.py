# First Duplicate Value 🔵
# Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that returns the first integer that appears more than once (when we read the array from left to right).
# If no integer appears more than once, your function should return -1.
# Note that you're allowed to mutate the input array.
# Sample Input
# array = [2, 1, 5, 3, 3, 2]
# Sample Output
# 3 // 3 is the first integer that appears more than once.

# Time O(n) | Space O(n)
def first_duplicate_value_first_try(array):
  uniques = set()
  for number in array:
    if number in uniques:
      return number
    else:
      uniques.add(number)
  return -1


# [2, 1, 5, 3, 3, 2,]
# we know that VALUES goes from 1 to n (length of array)
# we know we can mutate values
# if we can convert a VALUE to a fixed index we can know if that has been visited if that VALUE goes negative
# index = VALUE - 1, because arrays go from 0 to n-1, that is how we do the mapping to an index
# index = 2 - 1 = 1
# then 2 correlates to index 1, which goes negative
# [2, -1, 5, 3, 3, 2,]
# index = abs(-1) - 1 = 0
# then -1 correlates to index 0
# [-2, -1, 5, 3, 3, 2,]
# move pointer
# index = 5 - 1 = 4
# [-2, -1, 5, 3, -3, 2,]
# index = 3 - 1 = 2
# [-2, -1, -5, 3, -3, 2,]
# index = 3 - 1 = 2
# number at new index is < 0? -5 < 0? y, then we have visited it
# return the current value which is 3

# Time O(n) | Space O(1)
def first_duplicate_value(array):
  for number in array:
    index = abs(number) - 1
    at_index = array[index]
    if at_index < 0:
      return abs(number)
    else:
      array[index] *= -1
  return -1

print(first_duplicate_value([2, 1, 5, 3, 3, 2])) # 3
print(first_duplicate_value([2, 4, 3, 5, 1])) # -1
print(first_duplicate_value([1, 2, 3, 4, 5, 6, 1])) # 1
print(first_duplicate_value([1, 2, 3, 4, 5, 6, 5, 1])) # 5

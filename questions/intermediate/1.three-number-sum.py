# Three Number Sum 🔵
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
# The numbers in each triplet should be ordered in ascending order and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
# If no three numbers sum up to the target sum, the function should return an empty array
# Sample Input: array = [12, 3, 1, 2, -6, 5, -8, 6], targetSum = 0
# Sample Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Time Complexity O(n*n) where n is the numbers of the array
# Space Complexity 0(n) where n is the number of three target sums
def threeNumberSum(array, targetSum):
  results = []
  array.sort()
  current_index = 0
  left = 1
  right = len(array) - 1
  right_number = array[right]

  while current_index < len(array) - 1:
    base = array[current_index]
    left_number = array[left]
    right_number = array[right]
    current_sum = base + left_number + right_number
    if current_sum == targetSum:
      results.append([base, left_number, right_number])
      left += 1
      right -= 1
    elif current_sum < targetSum:
      left += 1
    else:
      right -= 1
    if left >= right or right <= left:
      current_index += 1
      left = current_index + 1
      right = len(array) - 1

  return results

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(threeNumberSum([1, 2, 3], 6))
print(threeNumberSum([1, 2, 3], 7))

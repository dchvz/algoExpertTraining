# Move Element to End 🔵
# Write a function that takes in an array of integers and an integer. The function should move all instances of that integer in the array to the end of the array and return the array.
# The function should perform this in place (i.e., it should mutate the input array)
# and doesn't need to maintain the order of the other integers.
# Sample Input
# array = [2, 1, 2, 2, 2, 3, 4, 2]
# to_move = 2
# Sample Output
# [1, 3, 4, 2, 2, 2, 2, 2]

# Time Complexity O(n)
# Space Complexity O(1)
def move_element_to_end(array, to_move):
  left = 0
  right = len(array) - 1
  while left < right:
    current = array[left]
    last = array[right]
    if current == to_move:
      if last == to_move:
        right -= 1
      else:
        array[left] = last
        array[right] = to_move
        right -= 1
        left += 1
    else:
      left += 1
  return array

print(move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2)) # [1, 3, 4, 2, 2, 2, 2, 2]
print(move_element_to_end([1, 2, 4, 5, 6, 2, 2, 3, 2], 2)) # [1, 3, 4, 5, 6, 2, 2, 2, 2]
print(move_element_to_end([1, 2, 4, 5, 6, 3], 2)) # [1, 3, 4, 5, 6, 2]
print(move_element_to_end([2, 2, 2, 2, 2, 2, 2, 2], 2)) # [2, 2, 2, 2, 2, 2, 2, 2]

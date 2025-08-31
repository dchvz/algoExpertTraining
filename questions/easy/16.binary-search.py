# Binary Search 🟢
# Write a function that takes in a sorted array of integers as well as a target integer
# The function should use the binary search algorithm to determine if the target is contained in the array and should returns its index, otherwise return -1
# Sample Input: array = [0,1,21,33,45,45,61,71,72,73], target = 33
# Sample Output: 3

# Time Complexity O(logn) because we cut the array in half on every iteration
# Space Complexity O(1) we do not use auxiliary data structures
def binary_search(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer <= right_pointer:
        middle = int((left_pointer + right_pointer)/2)
        element_in_middle = array[middle]
        if target < element_in_middle:
            right_pointer = middle - 1
        elif target > element_in_middle:
            left_pointer = middle + 1
        else:
            return middle

    return -1

print(binary_search([1, 2, 3, 4, 5, 6], 4))
print(binary_search([1, 2, 3, 4, 5, 6], 10))
print(binary_search([1, 2, 3, 4, 5, 6], 1))
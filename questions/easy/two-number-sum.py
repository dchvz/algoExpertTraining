# Two Number Sum 🟢
# Write a function that takes a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input sum up to the target, the function should return them in an array, in any order
# If no two numbers sum up to the target sum, the function should return an empty array

# Example Input array = [1, 2, 3], targetSum = 4
# Example output [1, 3] or [3, 1]

# First Approach
# Time Complexity: O(n^2)
# For each number, ideal_complement in array is O(n), so total is O(n^2).
# Space Complexity: O(1)
# No extra data structures are used (ignoring output).
def two_number_sum_brute_force(array, target_sum):
    for number in array:
        ideal_complement = target_sum - number
        if ideal_complement in array and ideal_complement != number:
            return [number, ideal_complement]
    return []


# Second approach using an additional data structure
# Time Complexity: O(n)
# First loop: O(n) to build the hash table.
# Second loop: O(n) to check for complements (hash table lookup is O(1)).
# Space Complexity: O(n)
# The hash table stores up to n elements.
def two_number_sum(array, target_sum):
    hash_table = {}
    for number in array:
        hash_table[number] = number

    for number in hash_table:
        ideal_complement = target_sum - number
        if ideal_complement != number and ideal_complement in hash_table:
            return [number, ideal_complement]

    return []

ex1 = {
  "array": [4, 6, 1],
  "targetSum": 5
}

ex2 = {
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9],
  "targetSum": 17
}

ex3 ={
  "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15],
  "targetSum": 18
}

print(two_number_sum(ex1["array"], ex1["targetSum"]))
print(two_number_sum(ex2["array"], ex2["targetSum"]))
print(two_number_sum(ex3["array"], ex3["targetSum"]))
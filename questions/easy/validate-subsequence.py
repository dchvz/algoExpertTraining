# Validate Subsequence 🟢
# Given two non-empty arrays of integers, write a function that determines whether the second array is
# a subsequence of the first one
# A subsequence of an array is a set of numbers that appear in the same order as they do in the array,
# but not necessarily consecutively.

# Example Input: array = [1,4,7,9]
# Example Input: sequence = [4,7,9]
# Example Output: True

# I tried using a hash_table and an index to keep track of the positions
# It got too complex and some test cases did not pass, for example array = [1,1,1,1] and sequence [1,1,1]
# Time Complexity: O(n) because we loop over two arrays separately
# Space Complexity: O(n) because we store the indices in a hash table
def validate_subsequence_brute_force(array, sequence):
    hash_table = {}
    prev_index = -1
    for index, number in enumerate(array):
        hash_table[number] = index
    for number in sequence:
        if number not in hash_table:
            return False
        current_index = hash_table[number]
        if current_index <= prev_index:
            return False
        prev_index = current_index
    return True

# Second approach
# Time Complexity O(n) because we loop over the main array once
# Space Complexity: O(1) because we only keep track of the index
def validate_subsequence(array, sequence):
    sequence_index = 0
    for number in array:
        if number == sequence[sequence_index]:
            sequence_index += 1
        if sequence_index == len(sequence):
            return True
    return False


print(validate_subsequence([1, 4, 7, 9], [4, 7, 9]))  # True
print(validate_subsequence([1, 4, 7, 9], [4, 9]))     # False
print(validate_subsequence([1, 4, 7, 9], [1, 4, 7]))  # True

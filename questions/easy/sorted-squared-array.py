# Sorted Squared Array 🟢
# Write a function that takes in a non-empty array of integers that are sorted in ascending order
# Return an array of the same length with the squares of the original integers sorted in ascending order

# Time Complexity O(nlogn) in average case, because it sorts the array at the end (needed for the negatives)
# Space Complexity O(n) because we store an array of n elements, those being the squared numbers in the main array
def sorted_squared_array_brute_force(array):
    squared_array = []
    for number in array:
        squared_array.append(number*number)
    squared_array.sort()
    return squared_array

# Looping over both ends of the array using pointers was the best way to accomplish this in O(n)
# Time Complexity O(n) because we are looping over the main array and sorting in place
# Space Complexity O(n) because we store an array of n elements, those being the squared numbers in the main array
def sorted_squared_array(array):
    new_position = len(array) - 1
    right_pointer = len(array) - 1
    left_pointer = 0
    sorted_array = [0] * len(array)
    index = 0
    while index < len(array):
        right_number = array[right_pointer]
        left_number = array[left_pointer]
        if right_pointer == left_pointer:
            squared_number = left_number*left_number
            sorted_array[new_position] = squared_number
        if abs(right_number) > abs(left_number):
            right_pointer -= 1
            squared_number = right_number*right_number
            sorted_array[new_position]= right_number*right_number
        else:
            left_pointer +=1
            squared_number = left_number*left_number
            sorted_array[new_position]= left_number*left_number
        new_position -= 1
        index += 1

    return sorted_array

print(sorted_squared_array([-7, -3, 0, 1, 2, 3, 4, 5]))
print(sorted_squared_array([-5, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
print(sorted_squared_array([-10, -5, 0, 5, 10]))
# Insertion Sort 🟢
# Write a function that takes an array of integers and returns a sorted version of that array using the insertion sort algorithm
# Insertion sort works by dividing the array into a sorted and an unsorted part. It iterates through the unsorted part and inserts each element into the correct position in the sorted part.
# Visual explanation: https://www.geeksforgeeks.org/insertion-sort/
# Keep in mind that this sort happens in-place! It is more like a swap sort, separating the "sorted" array "conceptually", it does not mean creating a new one

# Time Complexity O(n) best case if already sorted
# Time Complexity O(n²) average case
# Space Complexity O(1) because the array gets sorted in place
def insertion_sort(array):
    for index in range(1, len(array)):
        cursor = index
        while cursor > 0 and array[cursor] < array[cursor-1]:
            swap(cursor, cursor -1, array)
            cursor -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# Code below is my first try
# Please be aware that it is not the best solution, this approach is way too imperative, while the first one is clearly more elegant
# The first approach is the suggested solution that improves space complexity
# I tried to implement the algorithm too literally, also an important part of this algorithm is that it sorts the elements in place!

# Time Complexity O(n²)
# Space Complexity O(n) where n is the number of elements in the array
def insertion_sort_first_attempt(array):
    sorted_array = [array[0]]
    next_insertion_index = 1
    while next_insertion_index < len(array):
        element_to_insert = array[next_insertion_index]
        insert_in_sorted_array(sorted_array, element_to_insert)
        next_insertion_index += 1
    return sorted_array


def insert_in_sorted_array(sorted_array, element_to_insert):
    for index in range(len(sorted_array) - 1, -1, -1):
        current_number = sorted_array[index]
        last_index_of_sorted_array = len(sorted_array) - 1
        is_last_element_of_sorted_array = index == last_index_of_sorted_array
        if element_to_insert < current_number:
            sorted_array[index] = element_to_insert
            if is_last_element_of_sorted_array:
                sorted_array.append(current_number)
            else:
                sorted_array[index + 1] = current_number
        elif is_last_element_of_sorted_array:
            sorted_array.append(element_to_insert)

    return sorted_array

print(insertion_sort_first_attempt([5, 2, 9, 1, 5, 6]))
print(insertion_sort_first_attempt([12, 11, 13, 5, 6]))
print(insertion_sort_first_attempt([1, 2, 3, 4, 5]))

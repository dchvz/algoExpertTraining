
# Selection Sort 🟢
# Write a function that takes in an array of integers and returns a sorted version of that array using the Selection Sort algorithm
# The selection sort algorithm works by iterating through the array and finding the smallest number in the array
# Then swapping that number with the number in the first position
# Then it continues iterating through the array starting at the second position, finding the smallest number
# and swapping it with the number in the second position
# It continues doing this until it reaches the end of the array

# Time Complexity O(n²) where n is the numbers in the array
# Space Complexity is O(1) because the sort happens in place
def selection_sort(array):
    for i in range(0, len(array)):
        smallest_index = find_smallest_number_index_in_array(i, array)
        smallest_number = array[smallest_index]
        current_number = array[i]
        array[i] = smallest_number
        array[smallest_index] = current_number

    return array

def find_smallest_number_index_in_array(index, array):
    min = array[index]
    min_index = index
    for i in range(index, len(array)):
        current_element = array[i]
        if (current_element < min):
            min = current_element
            min_index = i
    return min_index

print(selection_sort([141, 1, 17, -7, -17, -27, 18, 541, 8, 7]))
print(selection_sort([0, 0, 2, 5, 5]))
print(selection_sort([-1, -2, -3, -7, -17]))

# Bubble Sort 🟢
# Write a function that takes in an array of integers and returns a sorted version of that array using the Bubble Sort algorithm
# The bubble sort consists of swapping each value with the next value if they are in the wrong order
# Repeat that process for as long as there are swaps being made

# Time Complexity O(n) at best if already sorted, O(n²) in the worst case, meaning swapping all the elements or looping all of them multiple times
# Space Complexity O(1)
def bubble_sort(array):
    should_swap = True
    elements_to_check = len(array) - 1
    while should_swap:
        swaps = swap_array(array, elements_to_check)
        should_swap = swaps > 0
        elements_to_check -= 1
    return array


def swap_array(array, elements_to_check):
    swaps = 0
    for index in range(0, elements_to_check):
        current_number = array[index]
        next_number = array[index + 1]
        if current_number > next_number:
            array[index] = next_number
            array[index + 1] = current_number
            swaps +=1
    return swaps

print(bubble_sort([141, 1, 17, -7, -17, -27, 18, 541, 8, 7]))
print(bubble_sort([0, 0, 2, 5, 5]))
print(bubble_sort([-1, -2, -3, -7, -17]))

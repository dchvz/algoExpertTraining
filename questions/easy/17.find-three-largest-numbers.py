# Find Three Largest Numbers 🟢
# Write a function that takes in an array of at least three integers and without sorting the input array,
# returns a sorted array of the three largest integers in the input array
# Sample Input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7]
# Sample Output: [141, 541, 18]

# Time Complexity O(n)
# Space Complexity O(1) since we do not use auxiliary data structures
def find_three_largest_numbers(array):
    highest = float('-inf')
    middle = float('-inf')
    lowest = float('-inf')
    for number in array:
        if number > highest:
            lowest = middle
            middle = highest
            highest = number
        elif number > middle:
            lowest = middle
            middle = number
        elif number > lowest:
            lowest = number

    return [lowest, middle, highest]


print(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7]))
print(find_three_largest_numbers([0, 0, 2, 5, 5]))
print(find_three_largest_numbers([-1, -2, -3, -7, -17]))
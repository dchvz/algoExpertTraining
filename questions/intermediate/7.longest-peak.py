# Longest Peak 🔵
# Write a function that takes in an array of integers and returns the length of the longest peak in the array.
# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a
# tip (the highest value in the peak), at which point they become strictly decreasing.
# At least three integers are required to form a peak.
# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 3.
# To solve this problem, we can iterate through the array and keep track of the longest peak we find.
# Sample Input
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 1, 0]
# Sample Output
# 6 // 0, 10, 6, 5, -1, -3


# Time Complexity O(n) where n is the numbers in the array
# Space Complexity O(1) only a handful of numbers will be peaks, so its constant
def longest_peak(array):
    print('array', array)
    peaks = get_peaks(array)
    return get_highest_peak(peaks, array)

# Time Complexity O(n) where n is the numbers in the array
# Space Complexity O(1) only a handful of numbers will be peaks, so its constant
def get_peaks(array):
    peaks = []
    for i in range(1, len(array) - 1):
        current = array[i]
        prev = array[i-1]
        next = array[i+1]
        if current > prev and current > next:
            peaks.append(i)
    return peaks

# Time Complexity O(n)
# Space Complexity O(1)
def get_highest_peak(peaks, array):
    max_peak = 0
    for peak in peaks:
        current_peak = 3
        prev = array[peak-1]
        current = array[peak]
        next = array[peak+1]

        if peak - 2 >= 0 and array[peak -2] < prev:
            left_side = get_left_side(peak - 2, array)
            current_peak += left_side
        if peak +2 < len(array) and array[peak +2] < next:
            right_side = get_right_side(peak + 2, array)
            current_peak += right_side

        if current_peak > max_peak:
            max_peak = current_peak
    return max_peak

# Time Complexity O(n)
# Space Complexity O(1)
def get_right_side(index, array):
    peak_len = 0
    for i in range(index, len(array)):
        current = array[i]
        peak_len +=1
        if i + 1 < len(array):
            next = array[i + 1]
            if next >= current:
                break
    return peak_len

# Time Complexity O(n)
# Space Complexity O(1)
def get_left_side(index, array):
    peak_len = 0
    for i in range(index, -1, -1):
        current = array[i]
        past = array[i - 1]
        peak_len +=1
        if past >= current:
            break
    return peak_len

print(longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 1, 0])) # 6
print(longest_peak([1, 2, 3, 4, 5, 1])) # 6
print(longest_peak([5, 4, 3, 2, 1, 2, 1])) # 3
print(longest_peak([1, 2, 3, 2, 1, 2, 3, 2, 1])) # 5
print(longest_peak([1, 2, 3, 4, 5, 6, 10, -1])) # 8

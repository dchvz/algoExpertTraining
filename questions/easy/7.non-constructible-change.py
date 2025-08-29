# Non Constructible Change 🟢
# Given an array of positive integers representing coins, write a function that returns the minimum amount of change you cannot give
# Not all coins will be unique. If you are given no coins, the min change you can't create is 1
# Sample Input: [1, 2, 5]
# Sample Output: 4

# Time Complexity O(nlogn) because we are sorting the array
# Space Complexity O(1) because we did not use any auxiliary data structures

# How to come up with this solution?
# Sorting certainly makes it easier to identify gaps in the change
# After some testing, it was clear that if the next coin was greater than the current change + 1, then we cannot cover the gap
# My mistake here was not understanding the problem completely, which led me to ignore this solution
# Examples that could be useful: [2,3,6] the output should be 1, [1,2,4] the output should be 5, [1,1,1,1] the output should be 5

def non_constructible_change(coins):
    coins.sort()
    current_change = 0
    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin
    return current_change + 1

print(non_constructible_change([1, 2, 5]))  # Output: 4
print(non_constructible_change([1, 1, 1, 1]))  # Output: 5
print(non_constructible_change([1, 2, 4]))  # Output: 3
print(non_constructible_change([2, 3, 6]))  # Output: 1
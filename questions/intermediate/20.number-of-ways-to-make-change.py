# 🟦 Number of ways to make change
# Given an array of positive integers representing coin denominations and a single non-negative integer n representing a target amount of money,
# write a function that returns the number of ways to make change for that target amount using the given coin denominations.
# Note that you have an unlimited amount of coins of each denomination.
# Sample Input:
# n=6
# denoms=[1,5]
# Sample Output:
# 2 # 1*6, 1 + 5

# n = 6
# [1,5]
# expected 2
# 1*6
# 1 + 5

# ways  =  [1, 0, 0, 0, 0, 0, 0]
# mounts = [0, 1, 2, 3, 4, 5, 6]

# denom = 1
# ways[mount] += ways[mount-denom]
# ways[1] += ways[1-1] = 1
# ways  =  [1, 1, 1, 1, 1, 1, 1]
# mounts = [0, 1, 2, 3, 4, 5, 6]

# denom = 5
# ways[5] += ways[5-5] = 2
# ways[6] += ways[6-5] = 1
# what we try to say is
# the current ways for an amount += the difference between that amount and the denom
# ways  =  [1, 1, 1, 1, 1, 5, 1]
# mounts = [0, 1, 2, 3, 4, 5, 6]

# let's say that the number to reach was 7
# ways  =  [1, 1, 1, 1, 1, 2, 2, 2]
# mounts = [0, 1, 2, 3, 4, 5, 6, 7]
# the ways[7] += ways[7-5] or ways[2]

# Time Complexity O(a*b) where a is the coin denominations and b is the amounts between 0 and n
# Space Complexity O(b)
def number_of_ways_to_make_change(n, denoms):
  ways = [0] * (n + 1)
  ways[0] = 1
  amounts = list(range(0, n + 1))
  for denom in denoms:
    for amount in amounts:
      if denom <= amount:
        ways[amount] += ways[amount-denom]
  return ways[n]
# Overlapping Intervals 🔵
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
# Each interval is defined as a pair of integers where the first integer is the start of the interval and the second integer is the end of the interval.
# Note that the start of any interval will always be less than or equal to the end of that interval.
# Also note that the intervals aren't necessarily presented in a sorted order.
# Sample Input
# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
# Sample Output: [[1, 2], [3, 8], [9, 10]]
# Explanation:
# The intervals in the input list overlap as such:
# [3, 5], [4, 7], and [6, 8] all overlap with one another, and thus can be merged into the single interval [3, 8].
# Since the other intervals don't overlap with one another, the final output is [[1, 2], [3, 8], [9, 10]].

# [[1,2], [3,5], [4,7], [6,8], [9,10]]
# take current and next intervals, verify overlap
# 2 < 3 ? yes, no overlap
# append current [[1,2]]
# take current and next intervals, verify overlap
# [3,5] and [4,7]
# 5 < 4 no, there is overlap
# modify next interval from [4,7] -> [3,7]
# take current and next intervals, verify overlap
# [3,7] and [6,8]
# 7 < 6 no, there is overlap
# modify next interval from [6,8] -> [3,8]
# take current and next intervals, verify overlap
# [3,8] and [9,10]
# 8 < 9 yes, no overlap
# append current [[1,2], [3,8]]
# if we are in the last run of the loop and there is no overlap, append the next interval
#[[1,2], [3,8], [9,10]]

# [[-20, 30], [1,22]]
# 30 >= 1 yes
# [1,22] -> [-20, 22]
# this is flawed, because it should have been [-20, 30]
# add validation to check which should be the digit that goes last

# Time Complexity O(nlogn): where n is the number of intervals
# Space Complexity O(n)
def merge_overlapping_intervals(intervals):
  overlaps = []
  intervals.sort(key=lambda x: x[0])
  for i in range(0, len(intervals)):
    first = intervals[i]
    second = intervals[i + 1] if i + 1 < len(intervals) else [float('inf'),float('inf')]
    if has_overlap(first, second):
      last = second[1] if second[1] > first[1] else first[1]
      intervals[i+1] = [first[0], last]
    else:
      overlaps.append(first)
  return overlaps

def has_overlap(firstInterval, secondInterval):
  return firstInterval[1] >= secondInterval[0]


print(merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])) # [[1, 2], [3, 8], [9, 10]]
print(merge_overlapping_intervals([[1, 2], [3, 5], [7, 9], [8, 10], [12, 15], [14, 18]])) # [[1, 2], [3, 5], [7, 10], [12, 18]]
print(merge_overlapping_intervals([[1, 4], [7, 10], [3, 5]])) # [[1, 5], [7, 10]]

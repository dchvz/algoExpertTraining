
# Tandem Bicycle 🟢
# A tandem bicycle is a bicycle that's operated by two people. Both pedal, but the person that pedals faster dictates the speed of the bicycle
# Given two lists of positive integers containing the speeds of riders in red and blue shirts, the goal is to pair every rider wearing red and blue
# Write a function that returns the maximum possible total speed or the minimum possible total based on an input parameter 'fastest'
# If fastest = true, we want to maximize the total speed
# If fastest = false, we want to minimize the total speed
# Sample Input: red_shirt_speeds = [5, 5, 3, 9, 2], blue_shirt_speeds = [3, 6, 7, 2, 1], fastest = True
# Sample Output: 32

# Time Complexity O(nlogn) because we do sort the arrays
# Space Complexity O(1) because we do not use auxiliary data structures
def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    red_shirt_speeds.sort(reverse=True)
    if fastest:
        blue_shirt_speeds.sort()
    else:
        blue_shirt_speeds.sort(reverse=True)
    total_speed = 0
    for i in range(0, len(red_shirt_speeds)):
        red_speed = red_shirt_speeds[i]
        blue_speed = blue_shirt_speeds[i]
        total_speed += max(red_speed, blue_speed)
    return total_speed


print(tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
print(tandem_bicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
print(tandem_bicycle([1, 2, 1, 9, 12, 3], [3, 3, 4, 6, 1, 2], False))

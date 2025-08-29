# Class Photos 🟢
# Given two lists of heights, one for students wearing red shirts and one for students wearing blue shirts,
# determine if it's possible to arrange the students in two rows such that all students in the back row are taller
# than those in the front row.

# Sample Input: red_shirt_heights = [5, 6, 7], blue_shirt_heights = [4, 5, 6]
# Sample Output: True

# Time Complexity O(nlogn) because we need to short the input array
# Space Complexity O(1) since we do not use additional data structures
def class_photos(red_shirt_heights, blue_shirt_heights):
    red_shirt_heights.sort()
    blue_shirt_heights.sort()

    tallest_guy_in_red = red_shirt_heights[len(red_shirt_heights) - 1]
    tallest_guy_in_blue = blue_shirt_heights[len(blue_shirt_heights) - 1]

    if tallest_guy_in_red > tallest_guy_in_blue:
        return all_back_row_students_are_taller(red_shirt_heights, blue_shirt_heights)
    else:
        return all_back_row_students_are_taller(blue_shirt_heights, red_shirt_heights)


def all_back_row_students_are_taller(back_row_guys, front_row_guys):
    for i in range(0, len(back_row_guys)):
        back_row_guy_is_taller = back_row_guys[i] > front_row_guys[i]
        if not back_row_guy_is_taller:
          return False
    return True

print(class_photos([5, 6, 7], [4, 5, 6]))
print(class_photos([5, 6, 7], [4, 8, 6]))
print(class_photos([5, 6, 7, 9], [4, 5, 6, 8]))

# Palindrome Check 🟢
# Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome
# A palindrome is defined as a string that is written the same forward and backward

# Time Complexity O(n) where n is the number of characters in the string
# Space Complexity O(1)
def is_palindrome(string):
  middle = int(len(string)/2)
  end = len(string) - 1
  for i in range(0, middle):
    current_letter = string[i]
    counter_letter = string[end]
    if current_letter != counter_letter:
      return False
    end -= 1
  return True

print(is_palindrome("abcdcba"))
print(is_palindrome("a"))
print(is_palindrome("ab"))
print(is_palindrome("abccba"))
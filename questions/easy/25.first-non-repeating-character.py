# First Non-Repeating Character 🟢
# Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.
# The first non-repeating character is the first character in a string that occurs only once.
# If a string doesn't have any non-repeating characters, your function should return -1.
# Sample Input: "abcdcaf"
# Sample Output: 1 (The first non-repeating character is "b" and is found at index 1)

# Time Complexity O(n) where n is the length of the string
# Space Complexity O(1) because the English alphabet contains 26 characters
def first_non_repeating_character(string):
  repetitions = {}
  singles = {}
  for index in range(0, len(string)):
    char = string[index]
    if char in singles:
      del singles[char]
    if char in repetitions:
      repetitions[char] += 1
    else:
      repetitions[char] = 1
      singles[char] = index
  first_key = next(iter(singles.values())) if singles else -1
  return first_key

print(first_non_repeating_character("abcdcaf"))
print(first_non_repeating_character("abcabc"))
print(first_non_repeating_character("aabbcc"))
print(first_non_repeating_character("a"))
print(first_non_repeating_character(""))
print(first_non_repeating_character("abacabad"))


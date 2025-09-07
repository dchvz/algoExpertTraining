# Common Characters 🟢
# Write a function that takes a list of strings and returns a list of characters that are common to all strings in the list, ignoring multiplicity
# The result can be in any order
# Sample Input: ["abc", "bcd", "cbad"]
# Sample Output: ["b", "c"]

# Sets can be really useful for this problem because they allow for checking intersection of characters easily
# Time Complexity O(n*m) where n is the number of strings and m is the length of the longest string
# Space Complexity O(m)
def commonCharacters(strings):
  common = set(strings[0])
  for s in strings[1:]:
    common &= set(s)   # intersection
  return list(common)

print(commonCharacters(["abc", "bcd", "cbad"]))
print(commonCharacters(["a", "b", "c"]))
print(commonCharacters(["a", "aa", "aaa", "aaaa", "aaaaa"]))

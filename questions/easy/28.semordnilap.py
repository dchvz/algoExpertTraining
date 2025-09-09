# Semordnilap 🟢
# A semordnilap is a word or phrase that spells a different word or phrase backwards. For example, "stressed" is "desserts" backwards.
# Write a function that takes in a list of unique words and returns a list of all the semordnilap pairs in the list.
# The order of the returned pairs and the order of the words in each pair does not matter.
# Each semordnilap pair should only be included once, and a word should not be paired with itself.
# You can assume that all words are in lowercase.
# Sample Input: ["diaper", "abc", "test", "cba", "repaid"]
# Sample Output: [["diaper", "repaid"], ["abc", "cba"]

# Time Complexity 0(n*m) where n is the number of words and m is the length of the longest word
# Space Complexity O(n*m) where n is the number of words and m is the length of the longest word
def semordnilap(words):
  word_set = set(words)
  found_pairs = set()
  semordnilap_pairs = []
  for word in word_set:
    reversed_word = word[::-1]
    if reversed_word in word_set and reversed_word not in found_pairs and word != reversed_word:
      semordnilap_pairs.append([word, reversed_word])
      found_pairs.add(word)
      found_pairs.add(reversed_word)
  return semordnilap_pairs

print(semordnilap(["diaper", "abc", "test", "cba", "repaid"]))
print(semordnilap(["stressed", "desserts", "drawer", "reward"]))
print(semordnilap(["hello", "world"]))
print(semordnilap(["racecar", "level", "rotor", "kayak"]))

# Generate Document 🟢
# You're given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters
# To generate the document, you can use each character in the available characters string as many times as you'd like. For example, if the available characters string consists of "abcabc" and the document string consists of "aabbccc" you can generate the document because the available characters string has two a's, two b's, and three c's
# Note: you can always generate the empty string
# Sample Input: "abcabc", "aabbc"
# Sample Output: True

# Time Complexity O(n+m) where n is the length of the document string, and m is the length of the characters string
# Space Complexity O(c) where n is the number of different characters in the characters string
def generate_document(characters, document):
  available_characters = {}
  for char in characters:
      if char in available_characters:
          available_characters[char] += 1
      else:
          available_characters[char] = 1

  for char in document:
      if char in available_characters and available_characters[char] > 0:
          available_characters[char] -= 1
      else:
          return False

  return True

print(generate_document("Bste!hetsi#dai", "Ahg!fd@"))
print(generate_document("Bste!hetsi#dai", "Ahg!fd@A"))
print(generate_document("abcabc", "aabbc"))
print(generate_document("a", "a"))
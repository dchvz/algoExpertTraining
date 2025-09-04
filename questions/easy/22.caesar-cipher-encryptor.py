# Caesar Cipher Encryptor 🟢
# Given a non-empty string of lowercase letters and a non-negative integer, representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key
# Note that letters should "wrap" around the alphabet; in other words, the letter z shifted by one returns the letter a
# Sample Input: "xyz", 2
# Sample Output: "zab"

# Time Complexity O(n) where n is the number of characters in the array
# Space Complexity O(1) the dictionary and alphabet variables are constant
def caesar_cipher_encryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_indices = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }
    new_string = ""
    if key > len(alphabet):
        key = key % len(alphabet)

    limit_to_wrap = len(alphabet) - key
    for char in string:
        letter_index = alphabet_indices[char]
        if letter_index >= limit_to_wrap:
            new_string += alphabet[letter_index - limit_to_wrap]
        else:
            new_string += alphabet[letter_index + key]
    return new_string

print(caesar_cipher_encryptor("xyz", 2))
print(caesar_cipher_encryptor("abc", 3))
print(caesar_cipher_encryptor("abc", 0))
print(caesar_cipher_encryptor("abc", 26))
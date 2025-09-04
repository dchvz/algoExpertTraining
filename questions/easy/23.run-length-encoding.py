# Run-Length Encoding 🟢
# Write a function that takes in a string and returns its run-length encoding
# From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run"
# For this problem, a run of data is any sequence of consecutive, identical characters. So the string "AAA" would be run-length encoded as "3A" (three A's)
# To make things more complicated, however, the input string can contain all sorts of special characters, including numbers
# And since encoded data must be decodable, this means that we can't have runs of more than 9 characters. In other words, the run-length encoding "12A" would be invalid
# For the input string "AAAAAAAAAAAA" (12 A's), the correct encoding would be "9A3A" (nine A's followed by three A's)
# Sample Input: "AAAAAAAAAAAAABBCCCCDD"
# Sample Output: "9A4A2B4C2D"

# Time Complexity O(n) where n is the characters in the array
# Space Complexity O(n) where n is the length of the input string
def run_length_encoding(string):
  repetitions = 1
  run_length_encode = ""
  for i in range(0, len(string)):
    current_letter = string[i]
    next_letter = string[i + 1] if i < len(string) - 1 else ""
    if current_letter == next_letter:
      if repetitions == 9:
        run_length_encode += f"{repetitions}{current_letter}"
        repetitions = 1
      else:
        repetitions += 1
    else:
      run_length_encode += f"{repetitions}{current_letter}"
      repetitions = 1
  return run_length_encode

print(run_length_encoding("AAAAAAAAAAAAABBCCCCDD"))
print(run_length_encoding("aA"))
print(run_length_encoding("122333"))
print(run_length_encoding("abc"))
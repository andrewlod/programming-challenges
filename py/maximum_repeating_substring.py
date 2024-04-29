"""
For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Examples:
Input: sequence = "ababc", word = "ab"
Output: 2

Input: sequence = "ababc", word = "ba"
Output: 1

Input: sequence = "ababc", word = "ac"
Output: 0

Problem source: LeetCode

Usage: maximum_repeating_substring.py <sequence> <word>
"""

import sys

def max_repeating(sequence: str, word: str) -> int:
  starting_points = {} #key: (ptr, repeat_count)
  n = len(word)
  max_repeat_count = 0

  for i, char in enumerate(sequence):
    if char == word[0]:
        starting_points[i] = [0, 0]

    to_delete = []
    for key, value in starting_points.items():
      if word[value[0]] == char:
        if value[0] == n-1:
          starting_points[key][1] += 1
          max_repeat_count = max(max_repeat_count, value[1])

        starting_points[key][0] = (value[0] + 1) % n
      else:
        to_delete.append(key)

    for key in to_delete:
      del starting_points[key]

  return max_repeat_count


if __name__ == "__main__":
  print(max_repeating(
    sys.argv[1],
    sys.argv[2]
  ))
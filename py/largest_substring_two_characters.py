"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Examples:
Input: s = "aa"
Output: 0

Input: s = "abca"
Output: 2

Input: s = "cbzxy"
Output: -1

Problem source: LeetCode

Usage: largest_substring_two_characters.py <str>
"""

import sys

def max_length_between_equal_characters(s: str) -> int:
  characters = {} #char: (idx, max)

  max_length = -1
  for i, char in enumerate(s):
    if char not in characters:
      characters[char] = [i, -1]
      continue

    idx, max_char_len = characters[char]
    current_len = i - idx - 1
    characters[char][1] = max(max_char_len, current_len)
    max_length = max(max_length, characters[char][1])

  return max_length


if __name__ == '__main__':
  print(max_length_between_equal_characters(sys.argv[1]))
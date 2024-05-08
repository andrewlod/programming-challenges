"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Examples:
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1

Problem source: LeetCode

Usage: first_unique_character.py <s>
"""

import sys

def first_uniq_char(s: str) -> int:
  unique_chars = {}
  repeated_chars = set()

  for i, char in enumerate(s):
    if char in repeated_chars:
      continue

    if char in unique_chars:
      del unique_chars[char]
      repeated_chars.add(char)
      continue

    unique_chars[char] = i

  if len(unique_chars) == 0:
    return -1

  return min(unique_chars.values())


if __name__ == '__main__':
  print(first_uniq_char(sys.argv[1]))
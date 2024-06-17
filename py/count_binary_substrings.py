"""
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Examples:
Input: s = "00110011"
Output: 6

Input: s = "10101"
Output: 4

Problem source: LeetCode

Usage: count_binary_substrings.py <s>
"""

import sys

def count_binary_substrings(s: str) -> int:
  zero_count = 0
  one_count = 0
  turn = s[0]
  count = 0

  for digit in s:
    if turn == digit:
      if digit == "0" and one_count > 0:
        turn = "1"
        zero_count = 0
          
      elif digit == "1" and zero_count > 0:
        turn = "0"
        one_count = 0

    if digit == "0":
      zero_count += 1
    elif digit == "1":
      one_count += 1

    if turn != digit:
      if (turn == "0" and zero_count >= one_count) or (turn == "1" and one_count >= zero_count):
        count += 1

  return count


if __name__ == "__main__":
  print(count_binary_substrings(sys.argv[1]))
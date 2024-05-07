"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Examples:
Input: s = "RLRRLLRLRL"
Output: 4

Input: s = "RLRRRLLRLL"
Output: 2

Input: s = "LLLLRRRR"
Output: 1

Problem source: LeetCode

Usage: split_balanced_strings.py <str_with_L_and_R>
"""

import sys

def balanced_string_split(s: str) -> int:
  count = 0
  num_splits = 0

  for char in s:
    if char == "R":
      count += 1
    else:
      count -= 1

    if count == 0:
      num_splits += 1

  return num_splits


if __name__ == "__main__":
  print(balanced_string_split(sys.argv[1]))
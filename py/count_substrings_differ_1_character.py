"""
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.

Examples:
Input: s = "aba", t = "baba"
Output: 6

Input: s = "ab", t = "bb"
Output: 3

Problem source: LeetCode

Usage: count_substrings_differ_1_character.py <s> <t>
"""

import sys

def count_substrings(s: str, t: str) -> int:
  m = len(s)
  n = len(t)

  equal_prev = [0] * (n+1)
  different_prev = [0] * (n+1)
  count = 0

  for i in range(m):
    equal_current = [0] * (n+1)
    different_current = [0] * (n+1)
    for j in range(n):
      if s[i] == t[j]:
        equal_current[j+1] = equal_prev[j] + 1
        different_current[j+1] = different_prev[j]
      else:
        different_current[j+1] = equal_prev[j] + 1

      count += different_current[j+1]

    equal_prev = equal_current
    different_prev = different_current

  return count


if __name__ == "__main__":
  print(count_substrings(sys.argv[1], sys.argv[2:]))
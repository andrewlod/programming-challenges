"""
Given a string s, find the length of the longest substring without repeating characters.

Examples:
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3

Problem source: LeetCode

Usage: longest_substring_no_repeating_characters.py <s>
"""

from collections import defaultdict
import sys

def length_of_longest_substring(s: str) -> int:
  chars = defaultdict(int)
  start = 0
  end = 0
  max_len = 0

  for char in s:
    if char in chars and chars[char] > 0:
      while chars[char] > 0:
        chars[s[start]] -= 1
        start += 1

    end += 1
    chars[char] += 1
    max_len = max(max_len, end - start)

  return max_len


if __name__ == "__main__":
  print(length_of_longest_substring(sys.argv[1]))
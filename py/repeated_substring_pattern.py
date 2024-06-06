"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Examples:
Input: s = "abab"
Output: true

Input: s = "aba"
Output: false

Input: s = "abcabcabcabc"
Output: true

Problem source: LeetCode

Usage: repeated_substring_pattern.py <s>
"""

import sys

def repeated_substring_pattern(s: str) -> bool:
  n = len(s)
  for i in range(1, n//2+1):
    if n % i == 0 and s[:i] * (n//i) == s:
      return True
  
  return False


def repeated_substring_pattern_2(s: str) -> bool:
  return s in (s + s)[1:-1]


if __name__ == '__main__':
  print(repeated_substring_pattern(sys.argv[1]))
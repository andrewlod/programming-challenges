"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Examples:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Problem source: LeetCode

Usage: greatest_common_divisor.py <str1> <str2>
"""

import sys

def is_divisor(s: str, pattern: str) -> bool:
  current_ptr = 0

  for char in s:
    if char != pattern[current_ptr]:
      return False

    current_ptr = (current_ptr + 1) % len(pattern)

  return current_ptr == 0

def gcd_of_strings(str1: str, str2: str) -> str:
  divisor = ""
  min_len = min(len(str1), len(str2))

  for i in range(min_len):
    if str1[i] != str2[i]:
      return divisor

    substr1 = str1[:i+1]

    if is_divisor(str1, substr1) and is_divisor(str2, substr1):
      divisor = substr1

  return divisor


if __name__ == "__main__":
  print(gcd_of_strings(sys.argv[1], sys.argv[2]))
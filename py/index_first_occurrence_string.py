"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Examples:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Input: haystack = "leetcode", needle = "leeto"
Output: -1

Problem source: LeetCode

Usage: index_first_occurrence_string.py <haystack> <needle>
"""

from typing import Tuple
import sys

def compare_strs(haystack: str, start_idx: int, needle: str) -> Tuple[bool, int]: # matches, next start idx
  if start_idx + len(needle) > len(haystack):
    return (False, -1)

  next_occurrence = -1
  for i in range(1, len(needle)):
    if next_occurrence == -1 and haystack[start_idx + i] == needle[0]:
      next_occurrence = start_idx + i

    if haystack[start_idx + i] != needle[i]:
      return (False, next_occurrence if next_occurrence != -1 else start_idx + i)

  return (True, next_occurrence)

def str_str(haystack: str, needle: str) -> int:
  if len(needle) > len(haystack):
    return -1

  idx = 0
  while idx < len(haystack):
    if haystack[idx] == needle[0]:
      matches, next_occurrence = compare_strs(haystack, idx, needle)
      if matches:
        return idx

      idx = max(idx+1, next_occurrence)
    else:
      idx += 1

  return -1


if __name__ == "__main__":
  print(str_str(sys.argv[1], sys.argv[2]))
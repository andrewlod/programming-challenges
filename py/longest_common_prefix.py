"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Examples:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""

Problem source: LeetCode

Usage: longest_common_prefix.py <comma_separated_strs>
"""

from typing import List
import sys

def longest_common_prefix(strs: List[str]) -> str:
  idx = 0
  while True:
    if idx >= len(strs[0]):
      return strs[0][:idx]

    current_char = strs[0][idx]
    for s in strs:
      if idx >= len(s) or s[idx] != current_char:
        return s[:idx]

      idx += 1


if __name__ == "__main__":
  print(longest_common_prefix(sys.argv[1].split(",")))
"""
Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

Examples:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false

Problem source: LeetCode

Usage: check_string_is_prefix_of_array.py <s> <comma_separated_words>
"""

from typing import List
from utils import read_str_array
import sys

def is_prefix_string(s: str, words: List[str]) -> bool:
  s_ptr = 0
  
  for word in words:
    for char in word:
      if s_ptr >= len(s) or char != s[s_ptr]:
        return False
      
      s_ptr += 1

    if s_ptr >= len(s):
      return True

  return s_ptr >= len(s)


if __name__ == "__main__":
  print(is_prefix_string(sys.argv[1], read_str_array(sys.argv[2])))
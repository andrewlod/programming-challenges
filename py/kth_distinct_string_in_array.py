"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

Examples:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"

Input: arr = ["a","b","a"], k = 3
Output: ""

Problem source: LeetCode

Usage: kth_distinct_string_in_array.py <comma_separated_strs> <k>
"""

from typing import List
from collections import Counter
from utils import read_str_array
import sys

def kth_distinct(arr: List[str], k: int) -> str:
  counts = Counter(arr)

  for s in arr:
    if counts[s] == 1:
      k -= 1
      if k == 0:
        return s

  return ""


if __name__ == "__main__":
  print(kth_distinct(read_str_array(sys.argv[1]), int(sys.argv[2])))
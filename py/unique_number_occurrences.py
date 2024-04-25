"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Examples:
Input: arr = [1,2,2,1,1,3]
Output: true

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Problem source: LeetCode

Usage: unique_number_occurrences.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def unique_occurrences(arr: List[int]) -> bool:
  counts = {}

  for num in arr:
    if num not in counts:
      counts[num] = 0

    counts[num] += 1

  unique_counts = set()

  for count in counts.values():
    if count in unique_counts:
      return False

    unique_counts.add(count)

  return True


if __name__ == "__main__":
  print(unique_occurrences(read_int_array(sys.argv[1])))
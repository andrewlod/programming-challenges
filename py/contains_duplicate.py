"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Examples:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Problem source: LeetCode

Usage: contains_duplicate.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def contains_duplicate(nums: List[int]) -> bool:
  counts = set()

  for num in nums:
    if num not in counts:
      counts.add(num)
    else:
      return True

  return False


if __name__ == "__main__":
  print(contains_duplicate(read_int_array(sys.argv[1])))
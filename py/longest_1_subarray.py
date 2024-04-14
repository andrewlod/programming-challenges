"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Examples:
Input: nums = [1,1,0,1]
Output: 3

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5

Input: nums = [1,1,1]
Output: 2

Problem source: LeetCode

Usage: longest_1_subarray.py <comma_separated_numbers>
"""

from typing import List
from utils import read_int_array
import sys

def longest_subarray(nums: List[int]) -> int:
  largest = 0
  current_count = 0
  last_continuous_count = 0

  for num in nums:
    if num != 1:
      largest = max(largest, current_count)
      current_count -= last_continuous_count
      last_continuous_count = current_count
      continue

    current_count += 1

  largest = max(largest, current_count)

  if largest == len(nums):
    return largest - 1

  return largest


if __name__ == "__main__":
  print(longest_subarray(read_int_array(sys.argv[1])))
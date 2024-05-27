"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Examples:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23

Problem source: LeetCode

Usage: maximum_subarray.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def max_sub_array(nums: List[int]) -> int:
  max_so_far = float("-inf")
  max_ending_here = 0

  for num in nums:
    max_ending_here += num
    max_so_far = max(max_so_far, max_ending_here)
    if max_ending_here < 0:
      max_ending_here = 0

  return max_so_far


if __name__ == "__main__":
  print(max_sub_array(read_int_array(sys.argv[1])))
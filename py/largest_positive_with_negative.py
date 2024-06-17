"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

Examples:
Input: nums = [-1,2,-3,3]
Output: 3

Input: nums = [-1,10,6,7,-7,1]
Output: 7

Input: nums = [-10,8,6,7,-2,-3]
Output: -1

Problem source: LeetCode

Usage: largest_positive_with_negative.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_max_k(nums: List[int]) -> int:
  values = set()

  max_num = -1
  for num in nums:
    values.add(num)
    if -num in values:
      max_num = max(max_num, abs(num))

  return max_num


if __name__ == '__main__':
  print(find_max_k(read_int_array(sys.argv[1])))
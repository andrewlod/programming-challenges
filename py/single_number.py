"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1

Problem source: LeetCode

Usage: single_number.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def single_number(nums: List[int]) -> int:
  num = nums[0]

  for i in range(1, len(nums)):
    num = num ^ nums[i]

  return num


if __name__ == "__main__":
  print(single_number(read_int_array(sys.argv[1])))
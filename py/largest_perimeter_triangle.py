"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Examples:
Input: nums = [2,1,2]
Output: 5

Input: nums = [1,2,1,10]
Output: 0

Problem source: LeetCode

Usage: largest_perimeter_triangle.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def largest_perimeter(nums: List[int]) -> int:
  sorted_nums = sorted(nums, reverse=True)

  for i in range(len(sorted_nums)-2):
    a, b, c = sorted_nums[i:i+3]

    if a < b + c:
      return a + b + c

  return 0


if __name__ == "__main__":
  print(largest_perimeter(read_int_array(sys.argv[1])))
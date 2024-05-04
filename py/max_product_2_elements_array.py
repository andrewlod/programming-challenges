"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Examples:
Input: nums = [3,4,5,2]
Output: 12

Input: nums = [1,5,4,5]
Output: 16

Problem source: LeetCode

Usage: max_product_2_elements_array.py <comma_separated_nums>
"""

from heapq import _heapify_max, _heappop_max
from typing import List
from utils import read_int_array
import sys

def max_product(nums: List[int]) -> int:
  _heapify_max(nums)

  a = _heappop_max(nums)
  b = _heappop_max(nums)

  return (a-1) * (b-1)


if __name__ == '__main__':
  print(max_product(read_int_array(sys.argv[1])))
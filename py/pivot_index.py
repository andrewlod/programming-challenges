"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Examples:
Input: boarnums = [1,7,3,6,5,6]
Output: 3

Input: nums = [1,2,3]
Output: -1

Input: nums = [2,1,-1]
Output: 0

Problem source: LeetCode

Usage: pivot_index.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def pivot_index(nums: List[int]) -> int:
  right_sum = sum(nums) - nums[0]
  left_sum = 0

  if right_sum == left_sum:
    return 0

  left_sum += nums[0]

  for i, item in enumerate(nums[1:]):
    right_sum -= item

    if right_sum == left_sum:
      return i + 1

    left_sum += item

  return -1


if __name__ == "__main__":
  print(pivot_index(read_int_array(sys.argv[1])))
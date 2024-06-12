"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Examples:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

Problem source: LeetCode

Usage: move_zeroes.py <comma_separated_numbers>
"""

from typing import List
from utils import read_int_array
import sys

def move_zeroes(nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """

  non_zero_ptr = 0

  for i in range(len(nums)):
    if nums[i] != 0:
      nums[non_zero_ptr] = nums[i]

      if non_zero_ptr != i:
        nums[i] = 0
          
      non_zero_ptr += 1


def move_zeroes_2(nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  non_zero_ptr = 0

  for i, num in enumerate(nums):
    if num != 0:
      if i == non_zero_ptr:
        non_zero_ptr += 1
      else:
        nums[non_zero_ptr] = num
        non_zero_ptr += 1
        nums[i] = 0


if __name__ == "__main__":
  print(move_zeroes(read_int_array(sys.argv[1])))
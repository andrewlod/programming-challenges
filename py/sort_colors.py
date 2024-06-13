"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Examples:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Problem source: LeetCode

Usage: sort_colors.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def sort_colors(nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  zero_pointer = 0
  two_pointer = len(nums)-1

  i = 0
  while i <= two_pointer:
    if i > zero_pointer and nums[i] == 0:
      nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
      zero_pointer += 1
    elif i < two_pointer and nums[i] == 2:
      nums[two_pointer], nums[i] = nums[i], nums[two_pointer]
      two_pointer -= 1
    else:
      i += 1


if __name__ == "__main__":
  sort_colors(read_int_array(sys.argv[1]))
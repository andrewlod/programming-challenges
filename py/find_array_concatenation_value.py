"""
You are given a 0-indexed integer array nums.

The concatenation of two numbers is the number formed by concatenating their numerals.

For example, the concatenation of 15, 49 is 1549.
The concatenation value of nums is initially equal to 0. Perform this operation until nums becomes empty:

If there exists more than one number in nums, pick the first element and last element in nums respectively and add the value of their concatenation to the concatenation value of nums, then delete the first and last element from nums.
If one element exists, add its value to the concatenation value of nums, then delete it.
Return the concatenation value of the nums.

Examples:
Input: nums = [7,52,2,4]
Output: 596

Input: nums = [5,14,13,8,12]
Output: 673

Problem source: LeetCode

Usage: find_array_concatenation_value.py <comma_separated_nums>
"""

from typing import List
from math import floor, log10
from utils import read_int_array
import sys

def find_the_array_conc_val(nums: List[int]) -> int:
  num = 0
  left = 0
  right = len(nums)-1

  while left < right:
    l_val = nums[left]
    r_val = nums[right]
    l_val *= (10 ** (1 + floor(log10(r_val))))
    num += l_val + r_val
    left += 1
    right -= 1

  if left == right:
    num += nums[left]

  return num


if __name__ == "__main__":
  print(find_the_array_conc_val(read_int_array(sys.argv[1])))
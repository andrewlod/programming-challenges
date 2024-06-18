"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Examples:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]

Input: nums = [-1,1]
Output: [1,-1]

Problem source: LeetCode

Usage: rearrange_array_elements_by_sign.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def rearrange_array(nums: List[int]) -> List[int]:
  result = [0] * len(nums)
  positive_ptr = 0
  negative_ptr = 1

  for num in nums:
    if num < 0:
      result[negative_ptr] = num
      negative_ptr += 2
    else:
      result[positive_ptr] = num
      positive_ptr += 2

  return result


if __name__ == "__main__":
  print(rearrange_array(read_int_array(sys.argv[1])))
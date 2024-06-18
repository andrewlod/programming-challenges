"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Examples:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2

Problem source: LeetCode

Usage: minimum_common_value.py <comma_separated_nums1> <comma_separated_nums2>
"""

from typing import List
from utils import read_int_array
import sys

def get_common(nums1: List[int], nums2: List[int]) -> int:
  ptr1 = 0
  ptr2 = 0
  m = len(nums1)
  n = len(nums2)

  while ptr1 < m and ptr2 < n:
    num1 = nums1[ptr1]
    num2 = nums2[ptr2]
    if num1 == num2:
      return num1
    elif num1 < num2:
      ptr1 += 1
    else:
      ptr2 += 1

  return -1


if __name__ == "__main__":
  print(get_common(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
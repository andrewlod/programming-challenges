"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Examples:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]

Problem source: LeetCode

Usage: difference_of_two_arrays.py <comma_separated_nums1> <comma_separated_nums2>
"""

from typing import List
from utils import read_int_array
import sys

def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
  different_1 = set(nums1)
  different_2 = set(nums2)

  for num in nums2:
    if num in different_1:
      different_1.remove(num)

  for num in nums1:
    if num in different_2:
      different_2.remove(num)

  return [list(different_1), list(different_2)]


if __name__ == '__main__':
  print(find_difference(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
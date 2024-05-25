"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Examples:
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

Input: nums = [11,13,15,17]
Output: 11

Problem source: LeetCode

Usage: min_rotated_sorted_array.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_min(nums: List[int]) -> int:
  left = 0
  right = len(nums)-1

  while nums[left] > nums[right]:
    midpoint = (left + right) // 2
    if nums[midpoint] >= nums[left]:
      left = midpoint + 1
    else:
      right = midpoint

  return nums[left]


if __name__ == '__main__':
  print(find_min(read_int_array(sys.argv[1])))
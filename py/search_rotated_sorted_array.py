"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Input: nums = [1], target = 0
Output: -1

Problem source: LeetCode

Usage: search_rotated_sorted_array.py <comma_separated_nums> <target>
"""

from typing import List
from utils import read_int_array
import sys

def search(nums: List[int], target: int) -> int:
  if len(nums) == 1:
    return 0 if nums[0] == target else -1

  left = 0
  right = len(nums)-1

  while nums[left] > nums[right]:
    midpoint = (left + right) // 2
    if nums[midpoint] >= nums[left]:
      left = midpoint + 1
    else:
      right = midpoint

  start_idx = left

  if nums[start_idx] <= target <= nums[-1]:
    left = start_idx
    right = len(nums)
  else:
    left = 0
    right = start_idx

  while left < right:
    midpoint = (left + right) // 2

    if nums[midpoint] == target:
      return midpoint

    if nums[midpoint] > target:
      right = midpoint
    else:
      left = midpoint + 1

  return -1


if __name__ == "__main__":
  print(search(read_int_array(sys.argv[1]), int(sys.argv[2])))
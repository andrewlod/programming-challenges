"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Examples:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

Problem source: LeetCode

Usage: first_last_position_sorted_array.py <comma_separated_nums> <target>
"""

from typing import List
import sys

def search_range(nums: List[int], target: int) -> List[int]:
  if len(nums) == 0:
    return [-1, -1]

  if len(nums) == 1 and target in nums:
    return [0, 0]

  l_min = 0
  r_min = len(nums)-1

  start_pos = None if nums[0] != target else 0

  while start_pos is None and l_min < r_min:
    midpoint = (r_min + l_min) // 2

    if nums[midpoint] != target and nums[midpoint+1] == target:
      start_pos = midpoint + 1
    elif nums[midpoint] >= target:
      r_min = midpoint
    else:
      l_min = midpoint + 1

  if start_pos is None:
    return [-1,-1]

  if nums[-1] == target:
    return [start_pos, len(nums)-1]
  
  l_max = start_pos
  r_max = len(nums)-1

  end_pos = start_pos

  while l_max < r_max:
    midpoint = (r_max + l_max) // 2

    if nums[midpoint] == target and nums[midpoint+1] != target:
      end_pos = midpoint
      break
    elif nums[midpoint] > target:
      r_max = midpoint
    else:
      l_max = midpoint + 1

  return [start_pos, end_pos]


if __name__ == "__main__":
  print(search_range(
    [int(num) for num in sys.argv[1].split(",")],
    int(sys.argv[2])
  ))
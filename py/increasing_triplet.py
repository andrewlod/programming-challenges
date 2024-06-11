"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Examples:
Input: nums = [1,2,3,4,5]
Output: true

Input: nums = [5,4,3,2,1]
Output: false

Input: nums = [2,1,5,0,4,6]
Output: true

Problem source: LeetCode

Usage: increasing_triplet.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def increasing_triplet(nums: List[int]) -> bool:
  best_size = 1
  best_min = nums[0]
  best_max = nums[0]
  current_size = best_size
  current_min = best_min
  current_max = best_max

  for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
      current_max = nums[i]
      current_size += 1
    else:
      current_size = 1
      current_max = nums[i]
      current_min = nums[i]

    if nums[i] > best_max:
      best_max = nums[i]
      best_size += 1
    elif best_min < nums[i] < best_max:
      best_max = nums[i]

    if current_size > best_size or (current_size == best_size and (current_max <= best_max and current_min <= best_min)):
      best_size = current_size
      best_min = current_min
      best_max = current_max

    if best_size == 3:
      return True

  return False


if __name__ == '__main__':
  print(increasing_triplet(read_int_array(sys.argv[1])))
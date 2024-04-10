"""
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

Examples:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Problem source: LeetCode

Usage: min_sub_array_len.py <target> <comma_separated_numbers>
"""

from typing import List
import sys

def min_sub_array_len(target: int, nums: List[int]) -> int:
  left_ptr = 0
  min_length = len(nums) + 1
  total_sum = 0

  for right_ptr, num in enumerate(nums):
      total_sum += num

      while total_sum >= target:
          min_length = min(min_length, right_ptr - left_ptr + 1)
          total_sum -= nums[left_ptr]
          left_ptr += 1

  if min_length > len(nums):
      return 0

  return min_length

if __name__ == "__main__":
  min_sub_array_len(int(sys.argv[1]), [
     int(num) for num in sys.argv[2].split(",")
  ])
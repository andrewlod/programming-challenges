"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Examples:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Problem source: LeetCode

Usage: max_consecutive_ones.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def longest_ones(nums: List[int], k: int) -> int:
  current_number_of_zeroes = 0
  current_length = 0
  maximum_length = 0
  start_idx = 0

  for i, num in enumerate(nums):
    if num == 1:
      current_length += 1
    else:
      while current_number_of_zeroes >= k:
        if nums[start_idx] == 0:
          current_number_of_zeroes -= 1

        start_idx += 1

      current_number_of_zeroes += 1
      current_length = i - start_idx + 1

    maximum_length = max(maximum_length, current_length)

  return maximum_length


if __name__ == "__main__":
  print(longest_ones(read_int_array(sys.argv[1]), int(sys.argv[2])))
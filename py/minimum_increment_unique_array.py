"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

Examples:
Input: nums = [1,2,2]
Output: 1

Input: nums = [3,2,1,2,1,7]
Output: 6

Problem source: LeetCode

Usage: minimum_increment_unique_array.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def min_increment_for_unique(nums: List[int]) -> int:
  sorted_nums = sorted(nums)

  moves = 0
  for i in range(1, len(sorted_nums)):
    if sorted_nums[i] <= sorted_nums[i-1]:
      moves += sorted_nums[i-1] - sorted_nums[i] + 1
      sorted_nums[i] = sorted_nums[i-1] + 1

  return moves


if __name__ == "__main__":
  print(min_increment_for_unique(read_int_array(sys.argv[1])))
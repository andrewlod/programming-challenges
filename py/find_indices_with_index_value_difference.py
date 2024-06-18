"""
You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

abs(i - j) >= indexDifference, and
abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

Note: i and j may be equal.

Examples:
Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
Output: [0,3]

Input: nums = [2,1], indexDifference = 0, valueDifference = 0
Output: [0,0]

Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
Output: [-1,-1]

Problem source: LeetCode

Usage: find_indices_with_index_value_difference.py <comma_separated_nums> <indexDifference> <valueDifference>
"""

from typing import List
from utils import read_int_array
import sys

def find_indices(nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
  n = len(nums)
  for i in range(n-indexDifference):
    for j in range(i+indexDifference, n):
      if abs(nums[i]-nums[j]) >= valueDifference:
        return [i, j]

  return [-1, -1]


if __name__ == "__main__":
  print(find_indices(read_int_array(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Examples:
Input: nums = [1,2,3,4], k = 5
Output: 2

Input: nums = [3,1,3,4,3], k = 6
Output: 1

Problem source: LeetCode

Usage: max_number_k_sum.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def max_operations(nums: List[int], k: int) -> int:
  num_counts = {}

  for num in nums:
    if not num in num_counts:
      num_counts[num] = 0

    num_counts[num] += 1

  count = 0

  for num in nums:
    complement = k - num
    if complement == num and num_counts[num] < 2:
      continue

    if complement in num_counts and num_counts[complement] > 0 and num_counts[num] > 0:
      count += 1
      num_counts[complement] -= 1
      num_counts[num] -= 1
      
  return count


if __name__ == "__main__":
  print(max_operations(read_int_array(sys.argv[1]), int(sys.argv[2])))
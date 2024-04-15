"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Examples:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000

Input: nums = [5], k = 1
Output: 5.00000

Problem source: LeetCode

Usage: max_average_subarray.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def find_max_average(nums: List[int], k: int) -> float:
  max_val = sum(nums[0:k])
  current_val = max_val
  first_ptr = 0

  for num in nums[k:]:
    current_val = current_val - nums[first_ptr] + num

    if current_val > max_val:
      max_val = current_val

    first_ptr += 1

  return max_val/k


if __name__ == "__main__":
  print(find_max_average(read_int_array(sys.argv[1]), int(sys.argv[2])))
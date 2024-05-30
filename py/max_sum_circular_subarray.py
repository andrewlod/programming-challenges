"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Examples:
Input: nums = [1,-2,3,-2]
Output: 3

Input: nums = [5,-3,5]
Output: 10

Input: nums = [-3,-2,-3]
Output: -2

Problem source: LeetCode

Usage: max_sum_circular_subarray.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def max_subarray_sum_circular(nums: List[int]) -> int:
  current_sum = 0
  current_max_sum = 0
  current_min_sum = 0
  max_sum = float('-inf')
  min_sum = float('inf')

  for num in nums:
    current_sum += num
    current_max_sum = max(num, current_max_sum + num)
    current_min_sum = min(num, current_min_sum + num)

    max_sum = max(max_sum, current_max_sum)
    min_sum = min(min_sum, current_min_sum)

  if max_sum < 0:
    return max_sum

  return max(max_sum, current_sum - min_sum)


if __name__ == '__main__':
  print(max_subarray_sum_circular(read_int_array(sys.argv[1])))
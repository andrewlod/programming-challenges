"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

Examples:
Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

Input: arr = [1], k = 1
Output: 1

Problem source: LeetCode

Usage: partition_array_maximum_sum.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def max_sum_after_partitioning(arr: List[int], k: int) -> int:
  dp = [-1] * len(arr)

  def calc(i: int) -> int:
    if i >= len(arr):
      return 0

    if dp[i] > -1:
      return dp[i]

    max_sum = 0
    for j in range(i, min(i + k, len(arr))):
      max_window_sum = calc(j + 1) + max(arr[i:j+1])*(j-i+1)
      max_sum = max(max_sum, max_window_sum)

    dp[i] = max_sum
    return max_sum

  return calc(0)


if __name__ == '__main__':
  print(max_sum_after_partitioning(read_int_array(sys.argv[1]), int(sys.argv[2])))
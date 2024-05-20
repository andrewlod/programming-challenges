"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Examples:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6

Problem source: LeetCode

Usage: num_subarrays_threshold.py <comma_separated_nums> <k> <threshold>
"""

from typing import List
from utils import read_int_array
import sys

def num_of_subarrays(arr: List[int], k: int, threshold: int) -> int:
  left = 0
  right = 0
  current_sum = 0
  count = 0

  for val in arr:
    if right - left < k:
      current_sum += val
      right += 1
      continue

    if (current_sum / k) >= threshold:
      count += 1

    current_sum -= arr[left]
    current_sum += val
    left += 1
    right += 1
      
  if (current_sum / k) >= threshold:
    count += 1

  return count


if __name__ == "__main__":
  print(num_of_subarrays(read_int_array(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
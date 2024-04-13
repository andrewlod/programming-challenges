"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Examples:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Problem source: LeetCode

Usage: k_largest_array.py <comma_separated_nums> <k>
"""

from heapq import _heapify_max, _heappop_max
from typing import List
from utils import read_int_array
import sys

def find_kth_largest(nums: List[int], k: int) -> int:
  _heapify_max(nums)
  
  for i in range(k-1):
    _heappop_max(nums)

  return _heappop_max(nums)


if __name__ == "__main__":
  print(find_kth_largest(read_int_array(sys.argv[1]), int(sys.argv[2])))
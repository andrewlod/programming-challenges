"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Examples:
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30

Problem source: LeetCode

Usage: max_subsequence_score.py <comma_separated_nums1> <comma_separated_nums2> <k>
"""

from typing import List
from functools import cmp_to_key
from heapq import heappop, heappush
from utils import read_int_array
import sys

def max_score(nums1: List[int], nums2: List[int], k: int) -> int:
  pairs = zip(nums1, nums2)
  sorted_pairs = sorted(pairs, key=cmp_to_key(lambda a, b: a[1] - b[1]), reverse=True)

  max_score = 0
  current_sum = 0
  min_heap = []

  for num1, num2 in sorted_pairs:
    current_sum += num1
    heappush(min_heap, num1)

    if len(min_heap) == k:
      max_score = max(max_score, current_sum * num2)
      current_sum -= heappop(min_heap)

  return max_score


if __name__ == "__main__":
  print(max_score(read_int_array(sys.argv[1]), read_int_array(sys.argv[2]), int(sys.argv[3])))
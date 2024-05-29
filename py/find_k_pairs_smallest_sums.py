"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Examples:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]

Problem source: LeetCode

Usage: find_k_pairs_smallest_sums.py <comma_separated_nums1> <comma_separated_nums2> <k>
"""

from heapq import heappush, heappop
from typing import List
from utils import read_int_array
import sys

def k_smallest_pairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
  pairs = []
  k_pairs = []

  for num in nums1:
    heappush(pairs, (num + nums2[0], 0))

  while k > 0 and pairs:
    pair_sum, pos_2 = heappop(pairs)
    val_1 = pair_sum - nums2[pos_2]
    k_pairs.append([val_1, nums2[pos_2]])

    if pos_2 < len(nums2)-1:
      pos_2 += 1
      heappush(pairs, (val_1 + nums2[pos_2], pos_2))

    k -= 1

  return k_pairs


if __name__ == "__main__":
  print(k_smallest_pairs(read_int_array(sys.argv[1]), read_int_array(sys.argv[2]), int(sys.argv[3])))
"""
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Examples:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]

Problem source: LeetCode

Usage: merge_2d_arrays.py "id1,val1 id2,val2 ..." "id1,val1 id2,val2 ..."
"""

from typing import List
from utils import read_int_matrix
import sys

def merge_arrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
  merged = []
  i = 0
  j = 0
  m = len(nums1)
  n = len(nums2)

  while i < m and j < n:
    id1, val1 = nums1[i]
    id2, val2 = nums2[j]
    if id1 == id2:
      merged.append([id1, val1 + val2])
      i += 1
      j += 1
    elif id1 < id2:
      merged.append([id1, val1])
      i += 1
    else:
      merged.append([id2, val2])
      j += 1

  while i < m:
    merged.append(nums1[i])
    i += 1

  while j < n:
    merged.append(nums2[j])
    j += 1

  return merged


if __name__ == "__main__":
  nums1 = read_int_matrix(sys.argv[1])
  nums2 = read_int_matrix(sys.argv[2:])
  print(merge_arrays(nums1, nums2))
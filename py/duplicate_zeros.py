"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Examples:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

Input: arr = [1,2,3]
Output: [1,2,3]

Problem source: LeetCode

Usage: duplicate_zeros.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def duplicate_zeros(arr: List[int]) -> None:
  """
  Do not return anything, modify arr in-place instead.
  """
  new_arr = []
  idx = 0
  while len(new_arr) < len(arr):
    new_arr.append(arr[idx])
    if arr[idx] == 0 and len(new_arr) < len(arr):
      new_arr.append(0)

    idx += 1

  arr[:] = new_arr[:]


if __name__ == "__main__":
  print(duplicate_zeros(read_int_array(sys.argv[1])))
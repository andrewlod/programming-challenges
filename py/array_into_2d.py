"""
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Examples:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]

Problem source: LeetCode

Usage: array_into_2d.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_matrix(nums: List[int]) -> List[List[int]]:
  arr = []
  for num in nums:
    found_set = False
    for num_set in arr:
      if num not in num_set:
        num_set.add(num)
        found_set = True
        break

    if not found_set:
      arr.append(set([num]))

  return [list(item) for item in arr]


if __name__ == "__main__":
  print(find_matrix(read_int_array(sys.argv[1])))
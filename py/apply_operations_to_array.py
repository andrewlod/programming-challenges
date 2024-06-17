"""
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.

Examples:
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]

Input: nums = [0,1]
Output: [1,0]

Problem source: LeetCode

Usage: apply_operations_to_array.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def apply_operations(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n-1):
    if nums[i] == nums[i+1]:
      nums[i] *= 2
      nums[i+1] = 0

  non_zero_ptr = 0
  for i in range(n):
    if nums[i] != 0:
      nums[non_zero_ptr] = nums[i]

      if i > non_zero_ptr:
        nums[i] = 0
          
      non_zero_ptr += 1


  return nums


if __name__ == "__main__":
  print(apply_operations(read_int_array(sys.argv[1])))
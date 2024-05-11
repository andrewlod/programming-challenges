"""
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

Examples:
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]

Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]

Problem source: LeetCode

Usage: arithmetic_subarrays.py <comma_separated_nums> <comma_separated_l> <comma_separated_r>
"""

from typing import List
from utils import read_int_array
import sys

def is_arithmetic(nums: List[int]):
  nums.sort()
  difference = nums[1] - nums[0]
  for i in range(2, len(nums)):
      if nums[i] - nums[i-1] != difference:
        return False

  return True

def check_arithmetic_subarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
  results = []
  for start, end in zip(l, r):
    results.append(is_arithmetic(nums[start:end+1]))

  return results


if __name__ == '__main__':
  print(check_arithmetic_subarrays(
    read_int_array(sys.argv[1]),
    read_int_array(sys.argv[2]),
    read_int_array(sys.argv[3])
  ))
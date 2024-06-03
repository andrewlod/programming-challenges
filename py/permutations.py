"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Examples:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]

Problem source: LeetCode

Usage: permutations.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def permute(nums: List[int]) -> List[List[int]]:
  permutations = []

  def backtrack(start):
    if start == len(nums):
      permutations.append(nums[:])
      return
    
    for i in range(start, len(nums)):
      nums[start], nums[i] = nums[i], nums[start]
      backtrack(start + 1)
      nums[start], nums[i] = nums[i], nums[start]

  backtrack(0)
  return permutations


if __name__ == "__main__":
  print(permute(read_int_array(sys.argv[1])))
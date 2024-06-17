"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Examples:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]

Input: nums = [2,3]
Output: [2,3]

Problem source: LeetCode

Usage: sort_array_by_parity_2.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def sort_array_by_parity_2(nums: List[int]) -> List[int]:
  wrong_evens = []
  wrong_odds = []

  for i, num in enumerate(nums):
    if num % 2 == 0 and i % 2 != 0:
      wrong_evens.append(i)
    elif num % 2 == 1 and i % 2 == 0:
      wrong_odds.append(i)

  for i, j in zip(wrong_evens, wrong_odds):
    nums[i], nums[j] = nums[j], nums[i]

  return nums


if __name__ == "__main__":
  print(sort_array_by_parity_2(read_int_array(sys.argv[1])))
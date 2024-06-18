"""
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
Return nums after the rearrangement.

Examples:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]

Problem source: LeetCode

Usage: partition_array_pivot.py <comma_separated_nums> <pivot>
"""

from typing import List
from utils import read_int_array
import sys

def pivot_array(nums: List[int], pivot: int) -> List[int]:
  result = []
  equals = []
  greater = []

  for num in nums:
    if num < pivot:
      result.append(num)
    elif num == pivot:
      equals.append(num)
    else:
      greater.append(num)

  
  return result + equals + greater


if __name__ == "__main__":
  print(pivot_array(read_int_array(sys.argv[1]), int(sys.argv[2])))
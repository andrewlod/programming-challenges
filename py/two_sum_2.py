"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Examples:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]

Problem source: LeetCode

Usage: two_sum_2.py <comma_separated_nums> <target>
"""

from typing import List
from utils import read_int_array
import sys

def two_sum(numbers: List[int], target: int) -> List[int]:
  left = 0
  right = len(numbers)-1

  while left < right:
    result = numbers[left] + numbers[right]
    if target > result:
      left += 1
    elif target < result:
      right -= 1
    else:
      return [left+1, right+1]

  return [left+1, right+1]


if __name__ == '__main__':
  print(two_sum(read_int_array(sys.argv[1]), int(sys.argv[2])))
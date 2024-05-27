"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Examples:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Problem source: LeetCode

Usage: longest_increasing_subsequence.py <comma_separated_nums>
"""

from typing import List
from heapq import heappop, heappush
from utils import read_int_array
import sys

def length_of_lis(nums: List[int]) -> int:
  dp = [1] * len(nums)
  best = 1

  for i in range(len(nums)-1, -1, -1):
    for j in range(i, len(nums)):
      if nums[i] < nums[j] and dp[j] >= dp[i]:
        dp[i] = dp[j] + 1
        if dp[i] > best:
          best = dp[i]

  return best

def length_of_lis_2(nums: List[int]) -> int:
  lengths = []
  heappush(lengths, (-1, -nums[-1]))

  for i in range(len(nums)-2, -1, -1):
    popped = []
    num = heappop(lengths)
    while lengths and num[1] > -nums[i]:
      popped.append(num)
      num = heappop(lengths)

    popped.append(num)
    if num[1] < -nums[i]:
      heappush(lengths, (num[0] - 1, -nums[i]))
    else:
      heappush(lengths, (-1, -nums[i]))

    for p in popped:
      heappush(lengths, p)

  return -heappop(lengths)[0]


if __name__ == '__main__':
  print(length_of_lis(read_int_array(sys.argv[1])))
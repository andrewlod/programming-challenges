"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Examples:
Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12

Problem source: LeetCode

Usage: house_robber.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys


def rob_dp(self, nums: List[int], idx: int, dp: List[int]):
  if idx >= len(nums):
    return 0
  
  if dp[idx] > -1:
    return dp[idx]

  result = max(
    nums[idx] + self.rob_dp(nums, idx + 2, dp),
    self.rob_dp(nums, idx + 1, dp)
  )

  dp[idx] = result
  return result

def rob(self, nums: List[int]) -> int:
  dp = [-1] * len(nums)
  return self.rob_dp(nums, 0, dp)


if __name__ == "__main__":
  print(rob(read_int_array(sys.argv[1])))
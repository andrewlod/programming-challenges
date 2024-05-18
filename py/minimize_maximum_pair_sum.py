"""
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

Examples:
Input: nums = [3,5,2,3]
Output: 7

Input: nums = [3,5,4,2,4,6]
Output: 8

Problem source: LeetCode

Usage: minimize_maximum_pair_sum.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def min_pair_sum(nums: List[int]) -> int:
  n = len(nums)
  sorted_nums = sorted(nums)

  max_sum = float("-inf")

  for i in range(n//2):
    max_sum = max(sorted_nums[i] + sorted_nums[n-i-1], max_sum)

  return max_sum


if __name__ == "__main__":
  print(min_pair_sum(read_int_array(sys.argv[1])))
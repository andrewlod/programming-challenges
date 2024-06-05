"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Examples:
Input: nums = [1,1,1,1,1], target = 3
Output: 5

Input: nums = [1], target = 1
Output: 1

Problem source: LeetCode

Usage: target_sum.py <comma_separated_nums> <target>
"""

from typing import List
from utils import read_int_array
import sys

def find_target_sum_ways(nums: List[int], target: int) -> int:
  counts = {0: 1}

  for num in nums:
    new_counts = {}

    for n, cnt in counts.items():
      if (n + num) not in new_counts:
        new_counts[n + num] = cnt
      else:
        new_counts[n + num] += cnt
          
      if (n - num) not in new_counts:
        new_counts[n - num] = cnt
      else:
        new_counts[n - num] += cnt

    counts = new_counts

  if target not in counts:
    return 0

  return counts[target]


if __name__ == "__main__":
  print(find_target_sum_ways(read_int_array(sys.argv[1]), int(sys.argv[2])))
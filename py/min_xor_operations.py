"""
You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.

Examples:
Input: nums = [2,1,3,4], k = 1
Output: 2

Input: nums = [2,0,2,0], k = 0
Output: 0

Problem source: LeetCode

Usage: min_xor_operations.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def min_operations(nums: List[int], k: int) -> int:
  xor_result = nums[0]

  for num in nums[1:]:
    xor_result ^= num

  xor_result ^= k
  steps = 0
  while xor_result > 0:
    remainder = xor_result % 2
    if remainder == 1:
      steps += 1
    xor_result //= 2

  return steps


if __name__ == "__main__":
  print(min_operations(read_int_array(sys.argv[1]), int(sys.argv[2])))
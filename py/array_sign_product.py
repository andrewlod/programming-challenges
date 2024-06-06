"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Examples:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1

Input: nums = [1,5,0,2,-3]
Output: 0

Input: nums = [-1,1,-1,1,-1]
Output: -1

Problem source: LeetCode

Usage: array_sign_product.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def array_sign(nums: List[int]) -> int:
  product = 1

  for num in nums:
    if num == 0:
      return 0

    product *= num // abs(num)

  return product


if __name__ == "__main__":
  print(array_sign(read_int_array(sys.argv[1])))
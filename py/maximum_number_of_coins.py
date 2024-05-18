"""
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.

Examples:
Input: piles = [2,4,1,2,7,8]
Output: 9

Input: piles = [2,4,5]
Output: 4

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18

Problem source: LeetCode

Usage: maximum_number_of_coins.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def max_coins(piles: List[int]) -> int:
  sorted_piles = sorted(piles)

  i = 0
  j = len(piles)-1

  total = 0

  while i < j:
    i += 1
    total += sorted_piles[j-1]
    j -= 2

  return total


if __name__ == "__main__":
  print(max_coins(read_int_array(sys.argv[1])))
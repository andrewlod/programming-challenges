"""
You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.

Examples:
Input: nums = [5,4,2,3]
Output: [3,2,5,4]

Input: nums = [2,5]
Output: [5,2]

Problem source: LeetCode

Usage: minimum_number_game.py <comma_separated_nums>
"""

from heapq import heapify, heappop
from typing import List
from utils import read_int_array
import sys

def number_game(nums: List[int]) -> List[int]:
  heapify(nums)
  arr = []

  while nums:
    alice = heappop(nums)
    bob = heappop(nums)
    arr.append(bob)
    arr.append(alice)

  return arr


if __name__ == "__main__":
  print(number_game(read_int_array(sys.argv[1])))
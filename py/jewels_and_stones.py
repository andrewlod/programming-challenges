"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Examples:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Input: jewels = "z", stones = "ZZ"
Output: 0

Problem source: LeetCode

Usage: jewels_and_stones.py <jewels> <stones>
"""

from functools import reduce
import sys

def num_jewels_in_stones(jewels: str, stones: str) -> int:
  jewels_set = set(jewels)
  return reduce(lambda acc, val: acc + 1 if val in jewels_set else acc, stones, 0)


if __name__ == "__main__":
  print(num_jewels_in_stones(sys.argv[1], sys.argv[2]))
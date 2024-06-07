"""
You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Examples:
Input: n = 2
Output: 2

Input: n = 100
Output: 14

Problem source: LeetCode

Usage: egg_drop_n_floors.py <n>
"""

from math import ceil, sqrt
import sys

def two_egg_drop(n: int) -> int:
  i = ceil(sqrt(n))

  while (((i + 1) * i) / 2) < n:
    i += 1

  return i


if __name__ == '__main__':
  print(two_egg_drop(int(sys.argv[1])))
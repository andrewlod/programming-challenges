"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Examples:
Input: n = 2
Output: 2

Input: n = 3
Output: 3

Problem source: LeetCode

Usage: climbing_stairs.py <n>
"""

import sys

def climb_stairs(n: int) -> int:
  if n == 1:
    return 1

  last = 2
  second_to_last = 1

  for _i in range(n-3, -1, -1):
    temp = last + second_to_last
    second_to_last = last
    last = temp

  return last


if __name__ == '__main__':
  print(climb_stairs(int(sys.argv[1])))
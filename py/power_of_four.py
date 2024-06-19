"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Examples:
Input: n = 16
Output: true

Input: n = 5
Output: false

Input: n = 1
Output: true

Problem source: LeetCode

Usage: power_of_four.py <n>
"""

import sys

def is_power_of_four(n: int) -> bool:
  if n < 1:
    return False

  while n > 1:
    if n % 4 != 0:
      return False

    n //= 4

  return True


if __name__ == "__main__":
  print(is_power_of_four(int(sys.argv[1])))
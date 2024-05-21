"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Examples:
Input: n = 3
Output: 0

Input: n = 5
Output: 1

Input: n = 0
Output: 0

Problem source: LeetCode

Usage: factorial_trailing_zeroes.py <n>
"""

import sys

def trailing_zeroes(n: int) -> int:
  count_2 = 0
  count_5 = 0

  for i in range(2, n+1):
    temp_5 = i
    while temp_5 % 5 == 0:
      count_5 += 1
      temp_5 /= 5

    temp_2 = i
    while temp_2 % 2 == 0:
      count_2 += 1
      temp_2 /= 2

  return min(count_2, count_5)


if __name__ == '__main__':
  print(trailing_zeroes(int(sys.argv[1])))
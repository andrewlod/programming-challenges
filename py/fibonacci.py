"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Examples:
Input: n = 2
Output: 1

Input: n = 3
Output: 2

Input: n = 4
Output: 3

Problem source: LeetCode

Usage: fibonacci.py <n>
"""

import sys

def fib(n: int) -> int:
  if n < 2:
    return [0, 1][n]

  last = 1
  second_to_last = 1

  for i in range(2, n):
    temp = last
    last += second_to_last
    second_to_last = temp

  return last


if __name__ == "__main__":
  print(fib(int(sys.argv[1])))
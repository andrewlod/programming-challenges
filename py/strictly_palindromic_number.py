"""
An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.

Examples:
Input: n = 9
Output: false

Input: n = 4
Output: false

Problem source: LeetCode

Usage: strictly_palindromic_number.py <n>
"""

from typing import List
import sys

def to_base(n: int, base: int) -> List[int]:
  result = []
  while n > 0:
    result.append(n % base)
    n //= base

  return result

def is_number_palindrome(n: int, base: int) -> bool:
  based = to_base(n, base)
  return based == based[::-1]

def is_strictly_palindromic(n: int) -> bool:
  for i in range(2, n-1):
    if not is_number_palindrome(n, i):
      return False

  return True


if __name__ == "__main__":
  print(is_strictly_palindromic(int(sys.argv[1])))
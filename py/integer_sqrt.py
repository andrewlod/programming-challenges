"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Examples:
Input: x = 4
Output: 2

Input: x = 8
Output: 2

Problem source: LeetCode

Usage: integer_sqrt.py <x>
"""

import sys

def my_sqrt(x: int) -> int:
  if x <= 1:
    return x

  left = 1
  right = x//2

  while left < right:
    midpoint = (left + right)//2
    squared = midpoint * midpoint

    if x == squared:
      return midpoint
    
    if squared > x:
      right = midpoint
    else:
      left = midpoint + 1

  if left * left > x:
    return left-1
  
  return left


if __name__ == "__main__":
  print(my_sqrt(int(sys.argv[1])))
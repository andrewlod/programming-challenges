"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Examples:
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000

Problem source: LeetCode

Usage: pow.py <x> <n>
"""

import sys

def my_pow(x: float, n: int) -> float:
  if x == 0:
    return 0

  if n == 0:
    return 1

  if n > 0:
    if n % 2 == 0:
      return my_pow(x*x, n//2)
    
    return x * my_pow(x, n-1)
  
  return my_pow(1/x, abs(n))

if __name__ == "__main__":
  print(my_pow(float(sys.argv[1]), int(sys.argv[2])))
"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Examples:
Input: n = 4
Output: 4

Input: n = 25
Output: 1389537

Problem source: LeetCode

Usage: tribonacci.py <n>
"""

from collections import deque
import sys

def tribonacci(n: int) -> int:
  trib = deque([0,1,1])

  if n <= 2:
    return trib[n]

  current_sum = 2
  while n > 3:
    removed = trib.popleft()
    trib.append(current_sum)
    current_sum = 2 * current_sum - removed
    n -= 1

  return current_sum


if __name__ == "__main__":
  print(tribonacci(int(sys.argv[1])))
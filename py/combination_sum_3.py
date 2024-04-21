"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Examples:
Input: k = 3, n = 7
Output: [[1,2,4]]

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Input: k = 4, n = 1
Output: []

Problem source: LeetCode

Usage: combination_sum_3.py <k> <n>
"""

from typing import List
import sys

def try_combinations(digits: List[int], current: List[int], current_idx: int, k: int, n: int, combinations: List[int], visited):
  if len(current) == k:
    current_tuple = tuple(current)
    if current_tuple in visited:
      return

    visited.add(current_tuple)

    if sum(current) == n:
      combinations.append(current[:])
    return

  if current_idx >= len(digits):
    return

  current.append(digits[current_idx])
  for i in range(current_idx + 1, len(digits) - k + len(current) + 1):
    try_combinations(digits, current, i, k, n, combinations, visited)

  current.pop()

def combination_sum_3(k: int, n: int) -> List[List[int]]:
  max_digit = min(9, n-1)

  digits = list(range(1, max_digit + 1))
  current = []
  combinations = []
  visited = set()

  for i in range(len(digits) - k + 1):
    try_combinations(digits, current, i, k, n, combinations, visited)

  return combinations


if __name__ == "__main__":
  print(combination_sum_3(int(sys.argv[1]), int(sys.argv[2])))
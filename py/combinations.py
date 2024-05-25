"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Examples:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Input: n = 1, k = 1
Output: [[1]]

Problem source: LeetCode

Usage: combinations.py <n> <k>
"""

from typing import List
import sys

def backtrack(current_combination: List[int], idx: int, n: int, k: int, combinations: List[List[int]]):
  current_combination.append(idx)
  if k == 1:
    combinations.append(current_combination[:])
    current_combination.pop()
    return


  for i in range(idx+1, n-k+3):
    backtrack(current_combination, i, n, k-1, combinations)
  
  current_combination.pop()

def combine(n: int, k: int) -> List[List[int]]:
  current_combination = []
  combinations = []
  for i in range(1, n - k + 2):
    backtrack(current_combination, i, n, k, combinations)
  return combinations


if __name__ == '__main__':
  print(combine(int(sys.argv[1]), int(sys.argv[2])))
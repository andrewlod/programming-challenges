"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Examples:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Input: matrix = [["0"]]
Output: 0

Problem source: LeetCode

Usage: maximal_square.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def maximal_square(matrix: List[List[str]]) -> int:
  max_side = 0
  m = len(matrix)
  n = len(matrix[0])
  areas = [[0 for j in range(n+1)] for i in range(m+1)]

  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      if matrix[i][j] == "1":
        areas[i][j] = min(areas[i+1][j], areas[i][j+1], areas[i+1][j+1]) + 1
        max_side = max(max_side, areas[i][j])
  
  return max_side * max_side


if __name__ == "__main__":
  print(maximal_square(read_int_matrix("".join(sys.argv[1:]))))
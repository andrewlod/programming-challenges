"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Examples:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7

Problem source: LeetCode

Usage: count_square_submatrices_with_ones.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def count_squares(matrix: List[List[int]]) -> int:
  m = len(matrix)
  n = len(matrix[0])
  square_sizes = [[0 for j in range(n+1)] for i in range(m+1)]
  count = 0

  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      if matrix[i][j] == 1:
        square_sizes[i][j] = min(square_sizes[i+1][j], square_sizes[i][j+1], square_sizes[i+1][j+1]) + 1
        count += square_sizes[i][j]

  return count


if __name__ == "__main__":
  print(count_squares(read_int_matrix("".join(sys.argv[1:]))))
"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Examples:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Input: mat = [[5]]
Output: 5

Problem source: LeetCode

Usage: matrix_diagonal_sum.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def diagonal_sum(mat: List[List[int]]) -> int:
  n = len(mat)
  total = 0

  for i in range(n):
    if i == n//2 and n % 2 == 1:
      total += mat[i][i]
    else:
      total += mat[i][i] + mat[i][n-1-i]

  return total


if __name__ == "__main__":
  print(diagonal_sum(read_int_matrix("".join(sys.argv[1:]))))
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Examples:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Problem source: LeetCode

Usage: set_matrix_zeroes.py <comma_separated_row_1> <comma_separated_row_2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def set_zeroes(matrix: List[List[int]]) -> None:
  """
  Do not return anything, modify matrix in-place instead.
  """
  rows_to_clear = set()
  cols_to_clear = set()

  for i, row in enumerate(matrix):
    for j, val in enumerate(row):
      if val == 0:
        rows_to_clear.add(i)
        cols_to_clear.add(j)

  for row in rows_to_clear:
    for i in range(len(matrix[row])):
      matrix[row][i] = 0

  for col in cols_to_clear:
    for i in range(len(matrix)):
      matrix[i][col] = 0


if __name__ == '__main__':
  matrix = read_int_matrix("".join(sys.argv[1:]))
  set_zeroes(matrix)
  for row in matrix:
    print(row)
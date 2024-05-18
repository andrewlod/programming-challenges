"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Examples:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39

Input: grid = [[0]]
Output: 1

Problem source: LeetCode

Usage: score_after_flipping_matrix.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def flip_row(grid: List[List[int]], row: int):
  for i in range(len(grid[row])):
    grid[row][i] = 1 - grid[row][i]


def flip_col(grid: List[List[int]], col: int):
  for i in range(len(grid)):
    grid[i][col] = 1 - grid[i][col]


def get_row_value(row: List[int]) -> int:
  val = 0
  for num in row:
    val <<= 1
    val += num

  return val

def has_zero_majority(grid: List[List[int]], col: int) -> bool:
  zero_count = 0

  for i in range(len(grid)):
    if grid[i][col] == 0:
      zero_count += 1

  return zero_count > len(grid)//2


def matrix_score(grid: List[List[int]]) -> int:
  for i in range(len(grid)):
    if grid[i][0] == 0:
      flip_row(grid, i)

  for i in range(len(grid[0])):
    if has_zero_majority(grid, i):
      flip_col(grid, i)

  return sum(get_row_value(row) for row in grid)


if __name__ == '__main__':
  print(matrix_score(read_int_matrix("".join(sys.argv[1:]))))
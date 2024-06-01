"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Problem source: LeetCode

Usage: number_of_islands.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def fill_island(grid: List[List[str]], row: int, col: int):
  grid[row][col] = "0"

  if row > 0 and grid[row-1][col] == "1":
    fill_island(grid, row-1, col)

  if row < len(grid)-1 and grid[row+1][col] == "1":
    fill_island(grid, row+1, col)

  if col > 0 and grid[row][col-1] == "1":
    fill_island(grid, row, col-1)

  if col < len(grid[0])-1 and grid[row][col+1] == "1":
    fill_island(grid, row, col+1)

def num_islands(grid: List[List[str]]) -> int:
  count = 0

  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      if val == "1":
        count += 1
        fill_island(grid, i, j)

  return count


if __name__ == "__main__":
  print(num_islands(read_int_matrix("".join(sys.argv[1:]))))
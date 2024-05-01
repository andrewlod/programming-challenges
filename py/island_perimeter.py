"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Examples:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16

Input: grid = [[1]]
Output: 4

Input: grid = [[1,0]]
Output: 4

Problem source: LeetCode

Usage: island_perimeter.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def island_perimeter(grid: List[List[int]]) -> int:
  count = 0
  n = len(grid[0])
  m = len(grid)

  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      if val == 0:
        continue

      if j - 1 < 0 or grid[i][j-1] == 0:
        count += 1

      if j + 1 == n or grid[i][j+1] == 0:
        count += 1

      if i - 1 < 0 or grid[i-1][j] == 0:
        count += 1

      if i + 1 == m or grid[i+1][j] == 0:
        count += 1

  return count


if __name__ == '__main__':
  print(island_perimeter(read_int_matrix("".join(sys.argv[1:]))))
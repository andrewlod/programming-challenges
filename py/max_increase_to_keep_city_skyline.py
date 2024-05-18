"""
There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.

Examples:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35

Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
Output: 0

Problem source: LeetCode

Usage: max_increase_to_keep_city_skyline.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def max_increase_keeping_skyline(grid: List[List[int]]) -> int:
  max_cols = [max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
  max_rows = [max(row) for row in grid]

  total = 0
  
  for i, row in enumerate(grid):
    for j, val in enumerate(row):
      total += min(max_cols[j], max_rows[i]) - val

  return total


if __name__ == "__main__":
  print(max_increase_keeping_skyline(read_int_matrix("".join(sys.argv[1:]))))
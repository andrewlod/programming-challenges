"""
You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Examples:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Input: grid = [[0,2]]
Output: 0

Problem source: LeetCode

Usage: rotting_oranges.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from collections import deque
from utils import read_int_matrix
import sys

def has_fresh_oranges(grid: List[List[int]]):
  for row in grid:
    for value in row:
      if value == 1:
        return True

  return False

def oranges_rotting(grid: List[List[int]]) -> int:
  m = len(grid)
  n = len(grid[0])
  next_rotten_oranges = deque()

  # Get first batch of rotten oranges (minute 0)
  for i, row in enumerate(grid):
    for j, value in enumerate(row):
      if value == 2:
        next_rotten_oranges.append((i, j))
  
  minutes_elapsed = 0

  while next_rotten_oranges:
    next_rotten = deque()

    while next_rotten_oranges:
      i, j = next_rotten_oranges.popleft()

      if i > 0 and grid[i-1][j] == 1:
        grid[i-1][j] = 2
        next_rotten.append((i-1, j))

      if i < m-1 and grid[i+1][j] == 1:
        grid[i+1][j] = 2
        next_rotten.append((i+1, j))

      if j > 0 and grid[i][j-1] == 1:
        grid[i][j-1] = 2
        next_rotten.append((i, j-1))

      if j < n-1 and grid[i][j+1] == 1:
        grid[i][j+1] = 2
        next_rotten.append((i, j+1))

    if len(next_rotten) > 0:
      minutes_elapsed += 1

    next_rotten_oranges += next_rotten

  if has_fresh_oranges(grid):
    return -1

  return minutes_elapsed


if __name__ == "__main__":
  print(oranges_rotting(read_int_matrix(" ".join(sys.argv[1:]))))
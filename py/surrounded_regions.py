"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Examples:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Input: board = [["X"]]
Output: [["X"]]

Problem source: LeetCode

Usage: surrounded_regions.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List, Set, Tuple
from utils import read_int_matrix
import sys

def search_island(board: List[List[str]], i: int, j: int, visited: Set[Tuple[int, int]], found: bool):
  if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i, j) in visited or board[i][j] == "X":
    return

  if board[i][j] == "O" and (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1):
      found = True

  visited.add((i, j))

  found = found or search_island(board, i+1, j, visited, found)
  found = found or search_island(board, i-1, j, visited, found)
  found = found or search_island(board, i, j+1, visited, found)
  found = found or search_island(board, i, j-1, visited, found)

  return found

def solve(board: List[List[str]]) -> None:
  """
  Do not return anything, modify board in-place instead.
  """
  m = len(board)
  n = len(board[0])
  visited = set()

  for i in range(1, m-1):
    for j in range(1, n-1):
      if board[i][j] == "O":
        v = set()
        found = search_island(board, i, j, v, False)
        if not found:
          for row, col in v:
            board[row][col] = "X"
        else:
          visited.update(v)


if __name__ == "__main__":
  matrix = read_int_matrix("".join(sys.argv[1:]))
  solve(matrix)
  for row in matrix:
    print(row)
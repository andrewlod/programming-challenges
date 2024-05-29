"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Examples:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Problem source: LeetCode

Usage: valid_sudoku.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def is_valid_sudoku(board: List[List[str]]) -> bool:
  rows_values = [set() for _ in range(9)]
  cols_values = [set() for _ in range(9)]
  blocks_values = [[set() for _ in range(3)] for _ in range(3)]

  for i, row in enumerate(board):
    for j, val in enumerate(row):
      if val == ".":
        continue
      
      if val in rows_values[i] or val in cols_values[j] or val in blocks_values[i//3][j//3]:
        return False
      
      rows_values[i].add(val)
      cols_values[j].add(val)
      blocks_values[i//3][j//3].add(val)

  return True


if __name__ == "__main__":
  print(is_valid_sudoku(read_int_matrix(sys.argv[1:])))
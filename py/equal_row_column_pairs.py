"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Examples:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3

Problem source: LeetCode

Usage: equal_row_column_pairs.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def compare(grid: List[List[int]], row: int, col: int):
  for i in range(1, len(grid)):
    if grid[row][i] != grid[i][col]:
      return False

  return True

def equal_pairs(grid: List[List[int]]) -> int:
  equal_count = 0
  n = len(grid)

  columns_first = {}

  for i, val in enumerate(grid[0]):
    if val not in columns_first:
      columns_first[val] = []

    columns_first[val].append(i)

  for row in range(n):
    if grid[row][0] not in columns_first:
      continue

    for col in columns_first[grid[row][0]]:
      if compare(grid, row, col):
        equal_count += 1


  return equal_count

# Second solution: using tuples as dict keys
def equal_pairs_2(grid: List[List[int]]) -> int:
  row_counts = {}
  n = len(grid)
  count = 0

  for row in grid:
    row_tuple = tuple(row)
    if row_tuple not in row_counts:
      row_counts[row_tuple] = 1
    else:
      row_counts[row_tuple] += 1

  for i in range(n):
    col = tuple([grid[j][i] for j in range(n)])
    if col in row_counts:
      count += row_counts[col]


  return count


if __name__ == '__main__':
  print(equal_pairs_2(read_int_matrix("".join(sys.argv[1:]))))
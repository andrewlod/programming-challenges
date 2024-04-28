"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Examples:
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]

Problem source: LeetCode

Usage: pascal_triangle_2.py <row_index>
"""

from typing import List
import sys

def get_row(row_index: int) -> List[int]:
  if row_index < 2:
    return [[1], [1,1]][row_index]

  last_row = [1,1]

  for i in range(row_index-1):
    new_row = [1] * (i + 3)
    for j in range(1, i + 2):
      new_row[j] = last_row[j-1] + last_row[j]

    last_row = new_row

  return last_row


if __name__ == "__main__":
  print(get_row(int(sys.argv[1])))
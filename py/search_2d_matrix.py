"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Examples:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Problem source: LeetCode

Usage: search_2d_matrix.py "<comma_separated_row1> <comma_separated_row2> ..." <target>
"""

from typing import List
from utils import read_int_matrix
import sys

def search_matrix(matrix: List[List[int]], target: int) -> bool:
  m = len(matrix)
  n = len(matrix[0])
  start = 0
  end = m * n

  while start < end:
    midpoint = (start + end) // 2
    midpoint_row = midpoint // n
    midpoint_col = midpoint % n

    if matrix[midpoint_row][midpoint_col] == target:
      return True

    if matrix[midpoint_row][midpoint_col] > target:
      end = midpoint
    else:
      start = midpoint + 1
  
  return False


if __name__ == "__main__":
  print(search_matrix(read_int_matrix(sys.argv[1]), int(sys.argv[2])))
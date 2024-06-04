"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Examples:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Problem source: LeetCode

Usage: rotate_image.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def rotate(matrix: List[List[int]]) -> None:
  """
  Do not return anything, modify matrix in-place instead.
  """
  n = len(matrix)

  for i in range(n//2):
    for j in range(i, n-1-i):
      a = matrix[i][j]
      b = matrix[j][n-1-i]
      c = matrix[n-1-i][n-1-j]
      d = matrix[n-1-j][i]

      matrix[i][j] = d
      matrix[j][n-1-i] = a
      matrix[n-1-i][n-1-j] = b
      matrix[n-1-j][i] = c


if __name__ == "__main__":
  matrix = read_int_matrix("".join(sys.argv[1:]))
  rotate(matrix)
  print(matrix)
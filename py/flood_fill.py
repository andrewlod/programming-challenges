"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Examples:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]

Problem source: LeetCode

Usage: flood_fill.py "r1n1,r2n2 r2n1,r2n2 ..." <sr> <sc> <color>
"""

from typing import List
from utils import read_int_matrix
import sys

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  if image[sr][sc] == color:
    return image

  positions = [(sr, sc)]
  start_color = image[sr][sc]
  m = len(image)
  n = len(image[0])

  while positions:
    next_positions = []

    for row, col in positions:
      image[row][col] = color

      if row > 0 and image[row-1][col] == start_color:
        next_positions.append((row-1, col))

      if row < m-1 and image[row+1][col] == start_color:
        next_positions.append((row+1, col))

      if col > 0 and image[row][col-1] == start_color:
        next_positions.append((row, col-1))

      if col < n-1 and image[row][col+1] == start_color:
        next_positions.append((row, col+1))

    positions = next_positions
  
  return image


if __name__ == "__main__":
  print(flood_fill(read_int_matrix("".join(sys.argv[1])), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
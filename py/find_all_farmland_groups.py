"""
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

Examples:
Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]

Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]

Input: land = [[0]]
Output: []

Problem source: LeetCode

Usage: find_all_farmland_groups.py <comma_separated_0s_and_1s> <comma_separated_0s_and_1s> ...
"""

from typing import List, Tuple
from utils import read_int_matrix
import sys

def find_farmland(land: List[List[int]]) -> List[List[int]]:
  lands = []

  
  def get_land_size(x: int, x_end: int, y: int, y_end: int) -> Tuple[int, int, int, int]: # (start_x, start_y, end_x, end_y)
    final_x = x_end-1
    final_y = y_end-1
    
    for i in range(y + 1, y_end):
      if land[i][x] == 0:
        final_y = i-1
        break

    for j in range(x + 1, x_end):
      if land[y][j] == 0:
        final_x = j-1
        break

    return (y, x, final_y, final_x)

  def find_lands(x_start: int, x_end: int, y_start: int, y_end: int):
    for y in range(y_start, y_end):
      for x in range(x_start, x_end):
        if land[y][x] == 1:
          coords = get_land_size(x, x_end, y, y_end)
          lands.append(list(coords))
          
          find_lands(x_start, coords[1], coords[0] + 1, coords[2] + 1)

          if coords[3] < x_end-1:
            find_lands(coords[3] + 1, x_end, y_start, coords[2] + 1)
          
          if coords[2] < y_end-1:
            find_lands(x_start, x_end, coords[2] + 1, y_end)

          return

  find_lands(0, len(land[0]), 0, len(land))
  return lands


if __name__ == "__main__":
  land = read_int_matrix("".join(sys.argv[1:]))
  print(find_farmland(land))
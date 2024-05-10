"""
Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)

Returns the current value of the coordinate (row,col) from the rectangle.

Examples:
Input
  ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
  [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output
  [null,1,null,5,5,null,10,5]

Input
  ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
  [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
Output
  [null,1,null,100,100,null,20]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import List

class SubrectangleQueries:

  def __init__(self, rectangle: List[List[int]]):
    self.rectangle = rectangle

  def update_subrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
    for i in range(row1, row2+1):
      for j in range(col1, col2+1):
        self.rectangle[i][j] = newValue

  def get_value(self, row: int, col: int) -> int:
    return self.rectangle[row][col]
"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Examples:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11

Input: triangle = [[-10]]
Output: -10

Problem source: LeetCode

Usage: triangle.py <row1val1> <row2val1,row2val2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def minimum_total(triangle: List[List[int]]) -> int:
  if len(triangle) == 1:
    return triangle[0][0]

  numbers = triangle[-1]

  for i in range(len(triangle)-2, -1, -1):
    new_numbers = []

    for j, num in enumerate(triangle[i]):
      new_numbers.append(num + min(numbers[j], numbers[j+1]))

    numbers = new_numbers

  return numbers[0]


if __name__ == "__main__":
  print(minimum_total(read_int_matrix("".join(sys.argv[1:]))))
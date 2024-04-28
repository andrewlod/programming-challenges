"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Examples:
Input: num_rows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: num_rows = 1
Output: [[1]]

Problem source: LeetCode

Usage: pascal_triangle.py <num_rows>
"""

from typing import List
import sys

def generate(num_rows: int) -> List[List[int]]:
  result = [[1] * (i + 1) for i in range(num_rows)]

  for i in range(2, num_rows):
    for j in range(1, len(result[i])-1):
      result[i][j] = result[i-1][j-1] + result[i-1][j]

  return result


if __name__ == "__main__":
  print(generate(int(sys.argv[1])))
"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Examples:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Problem source: LeetCode

Usage: unique_paths_2.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> int:
  if obstacleGrid[0][0] == 1:
    return 0

  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  dp = [[0 for j in range(n)] for i in range(m)]
  dp[m-1][n-1] = 1

  for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
      if j < n-1 and obstacleGrid[i][j+1] == 0:
        dp[i][j] += dp[i][j+1]

      if i < m-1 and obstacleGrid[i+1][j] == 0:
        dp[i][j] += dp[i+1][j]

  return dp[0][0]


if __name__ == "__main__":
  print(unique_paths_with_obstacles(read_int_matrix("".join(sys.argv[1:]))))
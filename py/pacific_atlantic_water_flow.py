"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Examples:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Input: heights = [[1]]
Output: [[0,0]]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import List

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
  m = len(heights)
  n = len(heights[0])
  can_reach = [[[False, False] for i in range(n)] for i in range(m)] # [pacific, atlantic]
  possible = []

  for i in range(m):
    can_reach[i][0][0] = True
    can_reach[i][-1][1] = True

  for i in range(n):
    can_reach[0][i][0] = True
    can_reach[-1][i][1] = True

  for i in range(1, m):
    for j in range(1, n):
      current = heights[i][j]
      can_reach[i][j][0] = can_reach[i][j][0] or (heights[i-1][j] <= current and can_reach[i-1][j][0]) or (heights[i][j-1] <= current and can_reach[i][j-1][0])
      k = m-1-i
      l = n-1-j
      current_atlantic = heights[k][l]
      can_reach[k][l][1] = can_reach[k][l][1] or (heights[k+1][l] <= current_atlantic and can_reach[k+1][l][1]) or (heights[k][l+1] <= current_atlantic and can_reach[k][l+1][1])
  
  for i in range(m):
    for j in range(n):
      if can_reach[i][j][0] and can_reach[i][j][1]:
        possible.append([i, j])

  return possible
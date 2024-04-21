"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Examples:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1

Problem source: LeetCode

Usage: nearest_exit_maze.py <comma_separated_strings> <x,y>
"""

from typing import List
from utils import read_int_array, read_str_matrix
import sys

def check_exit(m: int, n: int, row: int, col: int) -> bool:
  return row == m-1 or row == 0 or col == n-1 or col == 0


def nearest_exit(maze: List[List[str]], entrance: List[int]) -> int:
  m = len(maze)
  n = len(maze[0])

  entrance = tuple(entrance)
  paths = [(entrance, 0)]

  while paths:
    new_paths = []
    for pos, steps in paths:
      if pos != entrance and check_exit(m, n, pos[0], pos[1]):
        return steps

      if pos[0] > 0 and maze[pos[0]-1][pos[1]] == ".":
        maze[pos[0]-1][pos[1]] = "+"
        new_paths.append(((pos[0]-1, pos[1]), steps + 1))

      if pos[0] < m-1 and maze[pos[0]+1][pos[1]] == ".":
        maze[pos[0]+1][pos[1]] = "+"
        new_paths.append(((pos[0]+1, pos[1]), steps + 1))

      if pos[1] > 0 and maze[pos[0]][pos[1]-1] == ".":
        maze[pos[0]][pos[1]-1] = "+"
        new_paths.append(((pos[0], pos[1]-1), steps + 1))

      if pos[1] < n-1 and maze[pos[0]][pos[1]+1] == ".":
        maze[pos[0]][pos[1]+1] = "+"
        new_paths.append(((pos[0], pos[1]+1), steps + 1))

    paths = new_paths
  
  return -1


if __name__ == "__main__":
  print(nearest_exit(read_str_matrix(sys.argv[1]), read_int_array(sys.argv[2])))
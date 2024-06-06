"""
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Examples:
Input: moves = "UD"
Output: true

Input: moves = "LL"
Output: false

Problem source: LeetCode

Usage: robot_return_to_origin.py <moves>
"""

from typing import List
import sys

def move_pos(v: List[int], idx: int, inc: int):
  v[idx] += inc

move = {
  "U": lambda v: move_pos(v, 0, 1),
  "D": lambda v: move_pos(v, 0, -1),
  "L": lambda v: move_pos(v, 1, -1),
  "R": lambda v: move_pos(v, 1, 1)
}

def judge_circle(moves: str) -> bool:
  pos = [0, 0]

  for m in moves:
    move[m](pos)

  return pos[0] == 0 and pos[1] == 0


if __name__ == "__main__":
  print(judge_circle(sys.argv[1]))
"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Examples:
Input: position = [1,2,3,4,7], m = 3
Output: 3

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999

Problem source: LeetCode

Usage: magnetic_force_between_two_balls.py <comma_separated_nums> <m>
"""

from typing import List
from utils import read_int_array
import sys

def max_distance(position: List[int], m: int) -> int:
  sorted_positions = sorted(position)
  min_distance = -1
  left = 1
  right = sorted_positions[-1] - sorted_positions[0]

  while left <= right:
    midpoint = left + (right - left) // 2
    last_position, balls = sorted_positions[0], 1
    for i in range(1, len(sorted_positions)):
      if sorted_positions[i] - last_position >= midpoint:
        last_position = sorted_positions[i]
        balls += 1

    if balls >= m:
      min_distance = midpoint
      left = midpoint + 1
    else:
      right = midpoint - 1

  return min_distance


if __name__ == "__main__":
  print(max_distance(read_int_array(sys.argv[1]), int(sys.argv[2])))
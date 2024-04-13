"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Examples:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Problem source: LeetCode

Usage: min_arrow_shots.py <comma_separated_row1> <comma_separated_row2> ...
"""

from functools import cmp_to_key
from typing import List
from utils import read_int_matrix
import sys

def overlap(coord1, coord2):
  return max(coord1[0], coord2[0]) <= min(coord1[1], coord2[1])


def find_min_arrow_shots(points: List[List[int]]) -> int:
  points.sort(key=cmp_to_key(lambda a, b: a[0] - b[0] if a[0] != b[0] else a[1] - b[1]))

  groups = 1
  current_group_range = points[0]

  for coords in points[1:]:
    if not overlap(current_group_range, coords):
      current_group_range = coords
      groups += 1
    else:
      current_group_range = (max(current_group_range[0], coords[0]), min(current_group_range[1], coords[1]))

  return groups


if __name__ == "__main__":
  print(find_min_arrow_shots(read_int_matrix(" ".join(sys.argv[1:]))))
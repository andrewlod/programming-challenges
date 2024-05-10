"""
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.

Examples:
Input: points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
Output: [3,2,2]

Input: points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
Output: [2,3,2,4]

Problem source: LeetCode

Usage: number_of_points_inside_circles.py "c1x,c1y,c1r c2x,c2y,c2r ..." "p1x,p1y p2x,p2y ..."
"""

from typing import List
from math import sqrt
from utils import read_int_matrix
import sys

def distance_to_circle(circle: List[int], point: List[int]) -> float:
  return sqrt((circle[0] - point[0]) ** 2 + (circle[1] - point[1]) ** 2)

def is_inside_circle(circle: List[int], point: List[int]) -> bool:
  return distance_to_circle(circle, point) <= circle[2]
        
def countPoints(points: List[List[int]], queries: List[List[int]]) -> List[int]:
  results = [0] * len(queries)
  for i, circle in enumerate(queries):
    for point in points:
      if is_inside_circle(circle, point):
        results[i] += 1

  return results


if __name__ == '__main__':
  print(countPoints(
    read_int_matrix(sys.argv[1]),
    read_int_matrix(sys.argv[2])
  ))
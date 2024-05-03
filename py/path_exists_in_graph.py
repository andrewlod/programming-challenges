"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Examples:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false

Problem source: LeetCode

Usage: path_exists_in_graph.py <n> "n1,n2 n1,n3 n3,n5 ..." <source> <destination>
"""

from typing import List
from utils import read_int_matrix
import sys

def valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
  if source == destination and n > source:
    return True

  if not edges:
    return False
  
  graph = {}
  for direction in edges:
    if direction[0] not in graph:
      graph[direction[0]] = set()
    
    if direction[1] not in graph:
      graph[direction[1]] = set()

    graph[direction[0]].add(direction[1])
    graph[direction[1]].add(direction[0])

  visited = set()
  to_visit = [source]

  while to_visit:
    next_to_visit = []

    for item in to_visit:
      if item in visited:
        continue

      visited.add(item)
      if destination in graph[item]:
        return True

      next_to_visit += list(graph[item])

    to_visit = next_to_visit

  return False


if __name__ == "__main__":
  print(valid_path(int(sys.argv[1]), read_int_matrix(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
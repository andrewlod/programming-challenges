"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Examples:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Problem source: LeetCode

Usage: min_reorder_routes.py <num_cities> <comma_separated_ connections>
"""

from typing import Dict, List
from utils import read_int_matrix
import sys

def find_changes(adj: Dict, visited: List[bool], num: int, changes: List[int]):
  visited[num] = True

  for connection, direction in adj[num]:
    if not visited[connection]:
      if direction == 1:
        changes[0] += 1

        find_changes(adj, visited, connection)

def min_reorder(n: int, connections: List[List[int]]) -> int:
  adj = [[] for i in range(n)]

  for conn_from, conn_to in connections:
    adj[conn_from].append((conn_to, 1))
    adj[conn_to].append((conn_from, 0))

  visited = [False] * n
  changes = [0]

  find_changes(adj, visited, 0, changes)
  return changes[0]


if __name__ == "__main__":
  print(min_reorder(int(sys.argv[1]), read_int_matrix(" ".join(sys.argv[2:]))))
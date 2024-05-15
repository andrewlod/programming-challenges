"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Examples:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]

Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]

Problem source: LeetCode

Usage: minimum_vertices_to_reach_all_nodes.py <n> "edge_from,edge_to edge_from,edge_to ..."
"""

from typing import List
from utils import read_int_matrix
import sys

def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
  connections_received = [False for i in range(n)]

  for _, node_to in edges:
    connections_received[node_to] = True

  return [i for i in range(n) if connections_received[i] == False]


if __name__ == "__main__":
  print(find_smallest_set_of_vertices(int(sys.argv[1]), read_int_matrix(sys.argv[2])))
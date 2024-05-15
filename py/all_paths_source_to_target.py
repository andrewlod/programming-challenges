"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Examples:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]

Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Problem source: LeetCode

Usage: all_paths_source_to_target.py <comma_separated_adjacencies_0> <comma_separated_adjacencies_1> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
  paths = []
  def dfs(i: int, path: List[int]):
    path.append(i)
    if i == len(graph)-1:
      paths.append(path[:])
      path.pop()
      return
        
    for node in graph[i]:
      dfs(node, path)

    path.pop()

  starting_path = []
  dfs(0, starting_path)
  return paths


if __name__ == "__main__":
  print(all_paths_source_target(read_int_matrix("".join(sys.argv[1:]))))
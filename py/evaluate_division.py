"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Examples:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Problem source: LeetCode

Usage: evaluate_division.py "a,b b,c c,d" 1.0,2.0,3.0 "a,c b,d d,a x,y"
"""

from typing import List
import sys

def query(a: str, b: str, graph, visited: List[str]) -> float:
  if a in visited or a not in graph or b not in graph:
    return -1.0

  visited.append(a)

  if b in graph[a]:
    return graph[a][b]

  for num in graph[a]:
    result = query(num, b, graph, visited)
    if result != -1.0:
      graph[a][b] = graph[a][num] * result
      return graph[a][num] * result

  return -1.0


def calc_equation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
  graph = {}

  for pair, value in zip(equations, values):
    num, denom = pair

    if num not in graph:
      graph[num] = {}

    if denom not in graph:
      graph[denom] = {}

    graph[num][denom] = value
    graph[denom][num] = 1.0 / value

  results = []

  for num, denom in queries:
    results.append(query(num, denom, graph, []))

  return results


if __name__ == "__main__":
  print(calc_equation(
    [
      row.split(",") for row in sys.argv[1].split(" ")
    ], 
    [float(val) for val in sys.argv[2].split(",")],
    [
      row.split(",") for row in sys.argv[3].split(" ")
    ]
  ))
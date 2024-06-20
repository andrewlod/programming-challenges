"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Examples:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"

Input: paths = [["A","Z"]]
Output: "Z"

Problem source: LeetCode

Usage: destination_city.py <from_city1,to_city1> <from_city2,to_city2> ...
"""

from typing import List
from utils import read_str_matrix
import sys

def dest_city(paths: List[List[str]]) -> str:
  outbound = set()
  cities = set()

  for from_city, to_city in paths:
    outbound.add(from_city)
    cities.add(from_city)
    cities.add(to_city)

  for city in cities:
    if city not in outbound:
      return city

  return ""
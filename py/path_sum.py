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

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def amount_of_sums(node: Optional[TreeNode], path: List[int], current_sum: int, target: int) -> int:
  if node is None:
    return 0

  new_sum = current_sum + node.val
  weight = 0

  if new_sum == target:
    weight += 1

  for num in path:
    new_sum -= num
    if new_sum == target:
      weight += 1
  
  path.append(node.val)
  new_sum = current_sum + node.val

  total_weight = weight + amount_of_sums(node.left, path, new_sum, target) + amount_of_sums(node.right, path, new_sum, target)

  path.pop()

  return total_weight

def path_sum(root: Optional[TreeNode], targetSum: int) -> int:
  if root is None:
    return 0

  path = []

  return amount_of_sums(root, path, 0, targetSum)
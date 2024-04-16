"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Examples:
Input: root = [1,7,0,7,-8,null,null]
Output: 2

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED max_level_sum.py
"""

from typing import Optional
from utils import TreeNode

def max_level_sum(root: Optional[TreeNode]) -> int:
  max_sum = root.val
  max_level = 1
  current_level = 1

  nodes = [root]

  while nodes:
    current_sum = 0
    next_nodes = []

    for node in nodes:
      current_sum += node.val

      if node.left:
        next_nodes.append(node.left)

      if node.right:
        next_nodes.append(node.right)

    if current_sum > max_sum:
      max_sum = current_sum
      max_level = current_level

    nodes = next_nodes
    current_level += 1
  
  return max_level


if __name__ == "__main__":
  pass
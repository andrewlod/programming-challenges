"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def average_of_levels(root: Optional[TreeNode]) -> List[float]:
  averages = []

  nodes = [root]
  while nodes:
    new_nodes = []
    avg = 0

    for node in nodes:
      avg += node.val

      if node.left:
        new_nodes.append(node.left)

      if node.right:
        new_nodes.append(node.right)

    averages.append(avg / len(nodes))
    nodes = new_nodes

  return averages
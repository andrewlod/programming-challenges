"""
Given the root of a binary tree, return the sum of values of its deepest leaves.

Examples:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def deepest_leaves_sum(root: Optional[TreeNode]) -> int:
  leaves_sum = 0
  nodes = [root]

  while nodes:
    next_nodes = []
    current_sum = 0
    for node in nodes:
      current_sum += node.val

      if node.left:
        next_nodes.append(node.left)

      if node.right:
        next_nodes.append(node.right)

    nodes = next_nodes
    leaves_sum = current_sum

  return leaves_sum
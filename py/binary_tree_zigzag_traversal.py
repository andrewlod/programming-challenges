"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
  if not root:
    return None
  
  nodes = [root]
  result = []
  reverse = False

  while nodes:
    new_nodes = []
    line = [None] * len(nodes)
    for i, node in enumerate(nodes):
      if reverse:
        line[-i-1] = node.val
      else:
        line[i] = node.val

      if node.left:
        new_nodes.append(node.left)

      if node.right:
        new_nodes.append(node.right)

    result.append(line)
    nodes = new_nodes
    reverse = not reverse

  return result
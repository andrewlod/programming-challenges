"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
  if not root:
    return []

  nodes = [root]
  values = [[root.val]]

  while nodes:
    new_nodes = []
    row = []

    for node in nodes:
      if node.left:
        new_nodes.append(node.left)
        row.append(node.left.val)

      if node.right:
        new_nodes.append(node.right)
        row.append(node.right.val)

    nodes = new_nodes
    if row:
      values.append(row)

  return values
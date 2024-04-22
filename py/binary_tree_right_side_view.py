"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Examples:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: []
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def right_side_view(root: Optional[TreeNode]) -> List[int]:
  if root is None:
      return []

  elements = []

  nodes = [root]
  while nodes:
    next_nodes = []

    current_node = None
    for node in nodes:
      if node.left is not None:
        next_nodes.append(node.left)

      if node.right is not None:
        next_nodes.append(node.right)

      current_node = node

    if current_node is not None:
      elements.append(current_node.val)

    nodes = next_nodes

  return elements


if __name__ == "__main__":
  pass
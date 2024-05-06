"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Examples:
Input: root = [1,2,3,4,5]
Output: 3

Input: root = [1,2]
Output: 1

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, Tuple
from utils import TreeNode

def traverse(node: Optional[TreeNode]) -> Tuple[int, int]:
  if node is None:
    return (0, 0)

  depth_left, max_depth_left = traverse(node.left)
  depth_right, max_depth_right = traverse(node.right)

  current_depth = depth_left + depth_right
  max_depth = max(depth_left, depth_right)
  return (1 + max_depth, max(current_depth, max_depth_left, max_depth_right))

def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
  return traverse(root)[1]
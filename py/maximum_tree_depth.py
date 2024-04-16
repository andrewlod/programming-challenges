"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

Problem source: LeetCode

Usage: maximum_tree_depth.py
"""

from typing import Optional
from utils import TreeNode

def depth_search(node: Optional[TreeNode], depth: int) -> int:
  if node is None:
    return depth

  leftSearch = depth_search(node.left, depth + 1)
  rightSearch = depth_search(node.right, depth + 1)

  return max(leftSearch, rightSearch)

def max_depth(root: Optional[TreeNode]) -> int:
  return depth_search(root, 0)

if __name__ == "__main__":
  pass
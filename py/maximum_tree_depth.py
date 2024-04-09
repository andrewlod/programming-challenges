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

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def depthSearch(node: Optional[TreeNode], depth: int) -> int:
  if node is None:
    return depth

  leftSearch = depthSearch(node.left, depth + 1)
  rightSearch = depthSearch(node.right, depth + 1)

  return max(leftSearch, rightSearch)

def maxDepth(root: Optional[TreeNode]) -> int:
  return depthSearch(root, 0)

if __name__ == "__main__":
  pass
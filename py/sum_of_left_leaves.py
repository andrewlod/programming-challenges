"""
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Examples:
Input: root = [3,9,20,null,null,15,7]
Output: 24

Input: root = [1]
Output: 0

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
  leaves_sum = 0

  def dfs(node: Optional[TreeNode], left: bool):
    nonlocal leaves_sum
    if not node:
      return

    if left and not node.left and not node.right:
      leaves_sum += node.val
      return

    dfs(node.left, True)
    dfs(node.right, False)

  dfs(root, False)

  return leaves_sum
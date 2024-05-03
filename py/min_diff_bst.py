"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Examples:
Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def min_diff_in_bst(root: Optional[TreeNode]) -> int:
  min_difference = 2147483647
  
  def dfs(node: Optional[TreeNode], max_number: int, min_number: int):
    nonlocal min_difference
    if not node:
      return
    
    min_number = min(min_number, node.val)
    max_number = max(max_number, node.val)

    if node.left:
      min_difference = min(min_difference, abs(min_number - node.left.val), abs(node.val - node.left.val))
      dfs(node.left, node.val, min_number)

    if node.right:
      min_difference = min(min_difference, abs(max_number - node.right.val), abs(node.val - node.right.val))
      dfs(node.right, max_number, node.val)

  dfs(root, root.val, root.val)
  return min_difference
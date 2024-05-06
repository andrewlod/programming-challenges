"""
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

Examples:
Input: root = [1,1,1,1,1,null,1]
Output: true

Input: root = [2,2,2,5,2]
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def traverse(node: Optional[TreeNode], last_value: int) -> bool:
  if node is None:
    return True

  if node.val != last_value:
    return False

  return traverse(node.left, last_value) and traverse(node.right, last_value)

def is_unival_tree(root: Optional[TreeNode]) -> bool:
  return traverse(root, root.val)
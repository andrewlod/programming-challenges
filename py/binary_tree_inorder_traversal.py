"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Examples:
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def traverse(node: Optional[TreeNode], values: List[int]):
  if not node:
    return

  traverse(node.left, values)
  values.append(node.val)
  traverse(node.right, values)

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
  values = []
  traverse(root, values)
  return values
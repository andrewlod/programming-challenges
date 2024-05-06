"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Examples:
Input: root = [1,null,2,3]
Output: [3,2,1]

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
  traverse(node.right, values)
  values.append(node.val)

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
  values = []
  traverse(root, values)
  return values
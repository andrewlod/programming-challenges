"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

Examples:
Input: root = [1,0,1,0,1,0,1]
Output: 22

Input: root = [0]
Output: 0

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def traverse(node: Optional[TreeNode], current_number: int) -> int:
  if not node:
    return 0

  current_number <<= 1
  current_number += node.val
  if not node.left and not node.right:
    return current_number
  
  return traverse(node.left, current_number) + traverse(node.right, current_number)

def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
  return traverse(root, 0)
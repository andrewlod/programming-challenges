"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

Examples:
Input: root = [1,2,3]
Output: 1

Input: root = [4,2,9,3,5,null,7]
Output: 15

Input: root = [21,7,14,1,1,2,2,3,3]
Output: 9

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, Tuple
from utils import TreeNode

def traverse(node: Optional[TreeNode]) -> Tuple[int, int]:
  if not node:
    return (0, 0)

  if not node.left and not node.right:
    return (0, node.val)

  sub_tilt_left, sub_sum_left = traverse(node.left)
  sub_tilt_right, sub_sum_right = traverse(node.right)
  tilt = abs(sub_sum_left - sub_sum_right)

  return (tilt + sub_tilt_left + sub_tilt_right, node.val + sub_sum_left + sub_sum_right)

def find_tilt(root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  
  return traverse(root)[0]
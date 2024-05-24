"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

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

def find_minimum_difference(node: TreeNode, min_val: int, max_val: int) -> int:
  values = []
  values.append(abs(node.val - min_val))
  values.append(abs(node.val - max_val))

  new_min_val = min(min_val, node.val)
  new_max_val = max(max_val, node.val)
  if node.left:
    values.append(find_minimum_difference(node.left, new_min_val, node.val))

  if node.right:
    values.append(find_minimum_difference(node.right, node.val, new_max_val))

  return min(values)

def get_minimum_difference(root: Optional[TreeNode]) -> int:
  return find_minimum_difference(root, 2147483647, -2147483648)
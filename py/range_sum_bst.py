"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Examples:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def sum_range(node: Optional[TreeNode], low: int, high: int) -> int:
  if node is None:
    return 0

  current_sum = 0
  if low <= node.val <= high:
    current_sum = node.val

  if node.val > low:
    current_sum += sum_range(node.left, low, high)

  if node.val < high:
    current_sum += sum_range(node.right, low, high)

  return current_sum


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
  return sum_range(root, low, high)
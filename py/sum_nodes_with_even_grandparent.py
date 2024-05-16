"""
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18

Input: root = [1]
Output: 0

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def search(node: Optional[TreeNode], parent: Optional[TreeNode]) -> int:
  if not node:
    return 0

  val = 0
  if parent and parent.val % 2 == 0:
    val += 0 if not node.left else node.left.val
    val += 0 if not node.right else node.right.val

  val += search(node.left, node)
  val += search(node.right, node)

  return val

def sum_even_grandparent(root: TreeNode) -> int:
  return search(root, None)
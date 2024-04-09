"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Examples:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Problem source: LeetCode

Usage: same_tree.py
"""

from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if (p is None and q is not None) or (p is not None and q is None) or (p.val != q.val):
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
  pass
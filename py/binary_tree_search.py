"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Examples:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def search_node(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
  if node is None:
    return None

  if node.val == val:
    return node

  if val < node.val:
    return search_node(node.left, val)

  return search_node(node.right, val)

def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
  return search_node(root, val)


if __name__ == "__main__":
  pass
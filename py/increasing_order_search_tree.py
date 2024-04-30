"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Examples:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Input: root = [5,1,7]
Output: [1,null,5,null,7]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def rearrange_tree(node: Optional[TreeNode], parent: Optional[TreeNode]) -> Optional[TreeNode]:
  if node is None:
    return None

  is_leftmost_node = node.left is None

  leftmost_node = rearrange_tree(node.left, node)
  node.left = None

  if node.right:
    node.right = rearrange_tree(node.right, parent)
  else:
    node.right = parent

  if is_leftmost_node:
    return node

  return leftmost_node

def increasing_bst(root: TreeNode) -> TreeNode:
  return rearrange_tree(root, None)
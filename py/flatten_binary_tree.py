"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Examples:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Input: root = []
Output: []

Input: root = [0]
Output: [0]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def _flatten(node: TreeNode, next_node: Optional[TreeNode]):
  if not node.left and not node.right:
    node.right = next_node
    return

  next_right_node = next_node
  if node.right:
    _flatten(node.right, next_node)
    next_right_node = node.right

  if node.left:
    _flatten(node.left, next_right_node)
    node.right = node.left
  
  node.left = None

def flatten(root: Optional[TreeNode]) -> None:
  """
  Do not return anything, modify root in-place instead.
  """
  if not root:
    return
  
  _flatten(root, None)
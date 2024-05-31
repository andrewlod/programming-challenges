"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Examples:
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def validate(node: TreeNode, max_value: int, min_value: int) -> bool:
  if node.left:
    if node.left.val >= node.val or node.left.val <= min_value or not validate(node.left, node.val, min_value):
      return False
  
  if node.right:
    if node.right.val <= node.val or node.right.val >= max_value or not validate(node.right, max_value, node.val):
      return False

  return True

def is_valid_bst(root: Optional[TreeNode]) -> bool:
  return validate(root, float('inf'), float('-inf'))
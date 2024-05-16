"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Examples:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Input: root = [0,null,1]
Output: [1,null,1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def search(node: Optional[TreeNode], current_sum: int) -> int:
  if not node:
    return 0

  values_sum = node.val + search(node.right, current_sum)
  node.val = values_sum + current_sum

  return values_sum + search(node.left, node.val)

def bst_to_gst(root: TreeNode) -> TreeNode:
  search(root, 0)
  return root
    
"""
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Examples:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Input: preorder = [1,3]
Output: [1,null,3]

Problem source: LeetCode

Usage: construct_bst_from_preorder.py <comma_separated_nums>
"""

from typing import List, Optional
from utils import TreeNode, read_int_array
import sys

def bst_from_preorder(preorder: List[int]) -> Optional[TreeNode]:
  i = 0

  def construct_tree(node: TreeNode, parent_val: int):
    nonlocal i, preorder
    if i >= len(preorder):
      return

    node.val = preorder[i]
    i += 1
    
    if i >= len(preorder):
      return
    
    if preorder[i] < node.val:
      node.left = TreeNode()
      construct_tree(node.left, node.val)
    
    if i < len(preorder) and preorder[i] < parent_val:
      node.right = TreeNode()
      construct_tree(node.right, parent_val)

  
  root = TreeNode()
  construct_tree(root, float('inf'))
  return root


if __name__ == '__main__':
  print(bst_from_preorder(read_int_array(sys.argv[1])))
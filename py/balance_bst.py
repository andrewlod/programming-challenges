"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Examples:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]

Input: root = [2,1,3]
Output: [2,1,3]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def balance_bst(root: TreeNode) -> TreeNode:
  sorted_values = []

  def get_sorted_values(node: Optional[TreeNode]):
    if not node:
      return

    get_sorted_values(node.left)
    sorted_values.append(node.val)
    get_sorted_values(node.right)


  def build_tree(node: TreeNode, values: List[int]):
    midpoint = len(values)//2
    left = values[:midpoint]
    right = values[midpoint+1:]

    node.val = values[midpoint]

    if left:
      node.left = TreeNode()
      build_tree(node.left, left)

    if right:
      node.right = TreeNode()
      build_tree(node.right, right)


  get_sorted_values(root)

  new_root = TreeNode()
  build_tree(new_root, sorted_values)

  return new_root
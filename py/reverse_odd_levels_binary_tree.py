"""
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

Examples:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]

Input: root = [7,13,11]
Output: [7,11,13]

Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def reverse_odd_levels(root: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root.left or not root.right:
    return root

  level = 0
  nodes = [root]

  while nodes:
    new_nodes = []
    value_stack = []

    for node in nodes:
      if level % 2 == 0 and node.left:
        value_stack.append(node.left.val)
        value_stack.append(node.right.val)

      if node.left:
        new_nodes.append(node.left)

      if node.right:
        new_nodes.append(node.right)

    if level % 2 == 0:
      for node in new_nodes:
        node.val = value_stack.pop()

    level += 1
    nodes = new_nodes

  return root
"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

Examples:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def is_cousins(root: Optional[TreeNode], x: int, y: int) -> bool:
  x_node = None
  y_node = None

  nodes = [root]
  level = 0
  while nodes:
    new_nodes = []

    for node in nodes:
      if node.left:
        new_nodes.append(node.left)
        if node.left.val == x:
          x_node = (level+1, node.val)
        elif node.left.val == y:
          y_node = (level+1, node.val)

      if node.right:
        new_nodes.append(node.right)
        if node.right.val == x:
          x_node = (level+1, node.val)
        elif node.right.val == y:
          y_node = (level+1, node.val)

    if x_node and y_node:
      return x_node[0] == y_node[0] and x_node[1] != y_node[1]

    level += 1
    nodes = new_nodes
  
  return False
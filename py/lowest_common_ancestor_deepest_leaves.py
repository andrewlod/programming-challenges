"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

Examples:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

Input: root = [1]
Output: [1]

Input: root = [0,1,3,null,2]
Output: [2]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def lca_deepest_leaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
  nodes = [root]
  root.parent = None
  lowest_nodes = []

  while nodes:
    new_nodes = []

    for node in nodes:
      if node.left:
        new_nodes.append(node.left)
        node.left.parent = node

      if node.right:
        new_nodes.append(node.right)
        node.right.parent = node

    if not new_nodes:
      lowest_nodes = nodes

    nodes = new_nodes

  if len(lowest_nodes) == 1:
    return lowest_nodes[0]

  while lowest_nodes:
    new_nodes = []
    parent = lowest_nodes[0].parent

    if not parent:
      return root

    found_parent = True

    for node in lowest_nodes:
      if node.parent.val != parent.val:
        found_parent = False

      new_nodes.append(node.parent)

    if found_parent:
      return parent

    lowest_nodes = new_nodes

  return parent
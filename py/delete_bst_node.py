"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Examples:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]

Input: root = [], key = 0
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, Tuple
from utils import TreeNode

def find_node(node: Optional[TreeNode], parent: Optional[TreeNode], key: int) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
  if node is None:
    return None, None

  if node.val == key:
    return node, parent

  node_left, parent_left = find_node(node.left, node, key)
  if node_left:
    return node_left, parent_left

  node_right, parent_right = find_node(node.right, node, key)
  return node_right, parent_right


def find_min_node(node: Optional[TreeNode], parent: Optional[TreeNode]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
  if not node.left:
    return node, parent

  return find_min_node(node.left, node)


def find_max_node(node: Optional[TreeNode], parent: Optional[TreeNode]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
  if not node.right:
    return node, parent

  return find_max_node(node.right, node)

def delete_selected_node(node: TreeNode, parent: Optional[TreeNode], key: int):
  if not node.left and not node.right and parent:
    if parent.left and parent.left.val == node.val:
      parent.left = None
    else:
      parent.right = None

    return

  if node.right:
    min_right, parent_min = find_min_node(node.right, node)
    if parent_min.val == node.val:
      node.right = min_right.right
    elif min_right.right:
      parent_min.left = min_right.right
    else:
      parent_min.left = None

    node.val = min_right.val
  else:
    max_left, parent_max = find_max_node(node.left, node)
    if parent_max.val == node.val:
      node.left = max_left.left
    elif max_left.left:
      parent_max.right = max_left.left
    else:
      parent_max.right = None

    node.val = max_left.val

def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
  node, parent = find_node(root, None, key)
  if node is None:
    return root

  if node.val == root.val and not root.left and not root.right:
    return None

  delete_selected_node(node, parent, key)

  return root


if __name__ == "__main__":
  pass
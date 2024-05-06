"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Examples:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def find_paths(node: Optional[TreeNode], path: List[int], paths: List[str]):
  if not node:
    return

  path.append(str(node.val))
  if not node.left and not node.right:
    paths.append("->".join(path))
    path.pop()
    return

  find_paths(node.left, path, paths)
  find_paths(node.right, path, paths)
  path.pop()

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
  path = []
  paths = []
  find_paths(root, path, paths)
  return paths
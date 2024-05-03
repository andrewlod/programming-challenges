"""
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Examples:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def find_target(root: Optional[TreeNode], k: int) -> bool:
  nums = set()
  nodes = [root]

  while nodes:
    new_nodes = []
    for node in nodes:
      if (k - node.val) in nums:
        return True

      nums.add(node.val)
      
      if node.left:
        new_nodes.append(node.left)

      if node.right:
        new_nodes.append(node.right)

    nodes = new_nodes

  return False
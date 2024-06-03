"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Examples:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Input: root = [1,2,3], targetSum = 5
Output: false

Input: root = [], targetSum = 0
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def find_sum(node: TreeNode, current_sum: int, target_sum: int) -> bool:
  current_sum += node.val

  if not node.left and not node.right:
    return current_sum == target_sum

  return (node.left and find_sum(node.left, current_sum, target_sum)) or (node.right and find_sum(node.right, current_sum, target_sum))

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
  if not root:
    return False

  return find_sum(root, 0, targetSum)
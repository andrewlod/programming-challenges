"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Examples:
Input: root = [1,2,3]
Output: 25

Input: root = [4,9,0,5,1]
Output: 1026

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""
from typing import Optional
from utils import TreeNode

def dfs(node: TreeNode, current_num: int) -> int:
  if not node.left and not node.right:
    return current_num * 10 + node.val

  paths_sum = 0
  current_num = current_num * 10 + node.val
  if node.left:
    paths_sum += dfs(node.left, current_num)

  if node.right:
    paths_sum += dfs(node.right, current_num)

  return paths_sum

def sumNumbers(root: Optional[TreeNode]) -> int:
  return dfs(root, 0)
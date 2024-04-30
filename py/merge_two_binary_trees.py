"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Examples:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def merge(node1: Optional[TreeNode], node2: Optional[TreeNode], result: TreeNode):
  if not node1 and not node2:
    return

  if not node1:
    result.left = node2.left
    result.right = node2.right
    return

  if not node2:
    result.left = node1.left
    result.right = node1.right
    return

  if node1.left or node2.left:
    val1 = node1.left.val if node1.left else 0
    val2 = node2.left.val if node2.left else 0
    result.left = TreeNode(val1 + val2)
    merge(node1.left, node2.left, result.left)

  if node1.right or node2.right:
    val1 = node1.right.val if node1.right else 0
    val2 = node2.right.val if node2.right else 0
    result.right = TreeNode(val1 + val2)
    merge(node1.right, node2.right, result.right)

def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
  if not root1 and not root2:
    return None

  val1 = root1.val if root1 else 0
  val2 = root2.val if root2 else 0
  result = TreeNode(val1 + val2)

  merge(root1, root2, result)
  return result

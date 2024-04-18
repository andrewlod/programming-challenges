"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Examples:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def get_leaf_values(node: Optional[TreeNode], leaf_values: List[int]):
  if node is None:
    return

  if not node.left and not node.right:
    leaf_values.append(node.val)
    return

  get_leaf_values(node.left, leaf_values)
  get_leaf_values(node.right, leaf_values)


def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
  leaves1 = []
  get_leaf_values(root1, leaves1)

  leaves2 = []
  get_leaf_values(root2, leaves2)

  if len(leaves1) != len(leaves2):
    return False

  for num1, num2 in zip(leaves1, leaves2):
    if num1 != num2:
      return False

  return True


if __name__ == "__main__":
  pass
"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Examples:
Input: root = [3,1,4,3,null,1,5]
Output: 4

Input: root = [3,3,null,4,2]
Output: 3

Input: root = [1]
Output: 1

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional, List
from utils import TreeNode

def good_search(node: Optional[TreeNode], path: List[int], previous_is_good: int) -> int:
  if node is None:
    return 0

  good = 1
  if not (previous_is_good and node.val > path[-1]):
    for num in path:
      if num > node.val:
        good = 0
        break

  path.append(node.val)
  result = good + good_search(node.left, path, good) + good_search(node.right, path, good)
  path.pop()

  return result


def good_nodes(root: TreeNode) -> int:
  path = []
  return good_search(root, path, 0)


if __name__ == "__main__":
  pass
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Examples:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Problem source: LeetCode

# The default tree is [3,1,4,null,2]
Usage: kth_smallest_bst.py <k> 
"""

from typing import Optional, List
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_to_sorted(node: Optional[TreeNode], arr: List[int], k: int):
  if node is None:
    return
  
  bst_to_sorted(node.left, arr, k)
  arr.append(node.val)

  if len(arr) >= k:
    return

  bst_to_sorted(node.right, arr, k)


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
  arr = []
  bst_to_sorted(root, arr, k)
  return arr[k-1]


if __name__ == "__main__":
   tree_node = TreeNode(3)
   tree_node.left = TreeNode(1)
   tree_node.left.right = TreeNode(2)
   tree_node.right = TreeNode(4)

   print(kth_smallest(
      tree_node, int(sys.argv[1])
   ))
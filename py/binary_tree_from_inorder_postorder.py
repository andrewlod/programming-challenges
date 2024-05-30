"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Examples:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Input: inorder = [-1], postorder = [-1]
Output: [-1]

Problem source: LeetCode

Usage: binary_tree_from_inorder_postorder.py <comma_separated_inorder> <comma_separated_postorder>
"""

from typing import Optional, List
from utils import TreeNode, read_int_array
import sys

def build(self, node: TreeNode, inorder: List[int], postorder: List[int]):
  if len(inorder) == 1:
    node.val = inorder[0]
    postorder.pop()
    return

  node.val = postorder.pop()
  inorder_idx = 0
  try:
    inorder_idx = inorder.index(node.val)
  except ValueError:
    inorder_idx = 0

  inorder_left = inorder[:inorder_idx]
  inorder_right = inorder[inorder_idx+1:]

  if inorder_right:
    node.right = TreeNode()
    self.build(node.right, inorder_right, postorder)
  
  if inorder_left:
    node.left = TreeNode()
    self.build(node.left, inorder_left, postorder)


def build_tree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
  if len(inorder) == 1:
    return TreeNode(val=inorder[0])

  root = TreeNode(postorder.pop())
  inorder_idx = inorder.index(root.val)
  inorder_left = inorder[:inorder_idx]
  inorder_right = inorder[inorder_idx+1:]

  if inorder_right:
    root.right = TreeNode()
    self.build(root.right, inorder_right, postorder)
  
  if inorder_left:
    root.left = TreeNode()
    self.build(root.left, inorder_left, postorder)

  return root


if __name__ == "__main__":
  inorder = read_int_array(sys.argv[1])
  postorder = read_int_array(sys.argv[2])
  root = build_tree(inorder, postorder)
  print(root)
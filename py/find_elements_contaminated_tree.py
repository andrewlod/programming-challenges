"""
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

Examples:
Input
  ["FindElements","find","find"]
  [[[-1,null,-1]],[1],[2]]
Output
  [null,false,true]

Input
  ["FindElements","find","find","find"]
  [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
  [null,true,true,false]

Input
  ["FindElements","find","find","find","find"]
  [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
  [null,true,false,false,true]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

class FindElements:
  def decontaminate(self, node: Optional[TreeNode]):
    if not node:
      return

    self.values.add(node.val)

    if node.left:
      node.left.val = 2 * node.val + 1
      self.decontaminate(node.left)

    if node.right:
      node.right.val = 2 * node.val + 2
      self.decontaminate(node.right)

  def __init__(self, root: Optional[TreeNode]):
    self.root = root
    self.root.val = 0
    self.values = set([])
    self.decontaminate(self.root)

  def find(self, target: int) -> bool:
    return target in self.values
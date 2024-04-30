"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Examples:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3

Input: tree = [7], target =  7
Output: 7

Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from utils import TreeNode

def get_target_copy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
  if original is None:
    return None

  if original.val == target.val:
    return cloned

  left_result = self.getTargetCopy(original.left, cloned.left, target)
  if left_result:
    return left_result

  return self.getTargetCopy(original.right, cloned.right, target)
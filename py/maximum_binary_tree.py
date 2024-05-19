"""
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

Examples:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]

Input:nums = [3,2,1]
Output: [3,null,2,null,1]

Problem source: LeetCode

Usage: maximum_binary_tree.py <comma_separated_nums>
"""

from typing import List, Optional
from utils import TreeNode, read_int_array
import sys

def max_idx(nums: List[int]) -> int:
  max_idx = 0
  max_val = nums[0]
  for i in range(1, len(nums)):
    if nums[i] > max_val:
      max_val = nums[i]
      max_idx = i

  return max_idx

def construct_tree(nums: List[int], node: TreeNode):
  idx = max_idx(nums)
  left = nums[:idx]
  right = nums[idx+1:]
  node.val = nums[idx]

  if left:
    node.left = TreeNode()
    construct_tree(left, node.left)

  if right:
    node.right = TreeNode()
    construct_tree(right, node.right)

def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
  root = TreeNode()
  construct_tree(nums, root)
  return root


if __name__ == "__main__":
  nums = read_int_array(sys.argv[1])
  root = construct_maximum_binary_tree(nums)
  print(root)
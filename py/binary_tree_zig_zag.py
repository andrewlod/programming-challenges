"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Examples:
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3

Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4

Input: root = [1]
Output: 0

Problem source: LeetCode

Usage: CURRENTLY NOT IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode
from enum import Enum

class Direction(Enum):
  LEFT = 0
  RIGHT = 1

def zig_zag(self, node: Optional[TreeNode], direction: Direction, depth: int):
  if not node:
    return depth - 1

  other_direction = Direction.LEFT if direction == Direction.RIGHT else Direction.RIGHT
  next_node = node.left if direction == Direction.LEFT else node.right
  other_node = node.right if direction == Direction.LEFT else node.left

  return max(
    self.zig_zag(next_node, other_direction, depth + 1),
    self.zig_zag(other_node, direction, 1)
  )

def longestZigZag(self, root: Optional[TreeNode]) -> int:
  return self.zig_zag(root, Direction.LEFT, 0)


if __name__ == "__main__":
  pass
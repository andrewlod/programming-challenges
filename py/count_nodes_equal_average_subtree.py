"""
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
Input: root = [4,8,5,0,1,null,6]
Output: 5

Input: root = [1]
Output: 1

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Tuple
from math import floor
from utils import TreeNode

def dfs_average(node: TreeNode) -> Tuple[int, int, int]: # (match_count, avg, value_count)
  if not node.left and not node.right:
    return (1, node.val, 1)

  match_count = 0
  value_sum = 0
  value_count = 0
  if node.left:
    match_left, avg_left, value_count_left = dfs_average(node.left)
    match_count += match_left
    value_count += value_count_left
    value_sum += avg_left * value_count_left
      
  if node.right:
    match_right, avg_right, value_count_right = dfs_average(node.right)
    match_count += match_right
    value_count += value_count_right
    value_sum += avg_right * value_count_right

  avg = round(value_sum + node.val) / (value_count + 1)
  if node.val == floor(avg):
    match_count += 1

  return (match_count, avg, value_count + 1)

def average_of_subtree(root: TreeNode) -> int:
  return dfs_average(root)[0]
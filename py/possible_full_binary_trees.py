"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Examples:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Input: n = 3
Output: [[0,0,0]]

Problem source: LeetCode

Usage: possible_full_binary_trees.py <n>
"""

from typing import List, Optional
from utils import TreeNode
import sys

def all_possible_fbt(n: int) -> List[Optional[TreeNode]]:
  results = {}

  def generate_trees(n: int):
    if n == 0 or n % 2 == 0:
      return []
    if n == 1:
      return [TreeNode(0)]

    if n in results:
      return results[n]
    
    result = []
    for left in range(1, n-1, 2):
      left_trees = generate_trees(left)
      right_trees = generate_trees(n-left-1)

      for left_tree in left_trees:
        for right_tree in right_trees:
          result.append(TreeNode(0, left=left_tree, right=right_tree))

    results[n] = result
    return result
  
  return generate_trees(n)


if __name__ == "__main__":
  print(all_possible_fbt(int(sys.argv[1])))
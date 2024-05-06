"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Examples:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import List
from utils import NAryNode

def traverse(node: NAryNode, values: List[int]):
  if not node:
    return

  values.append(node.val)
  for child in node.children:
    traverse(child, values)

def preorder(root: NAryNode) -> List[int]:
  values = []
  traverse(root, values)
  return values
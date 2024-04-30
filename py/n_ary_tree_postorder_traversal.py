"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Examples:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import List, Optional

# Definition for a N-Ary Node.
class NAryNode:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

def postorder(self, root: Optional[NAryNode]) -> List[int]:
  if root is None:
    return []

  if root.children is None:
    return [root.val]

  values = []
  for child in root.children:
    values += self.postorder(child)

  values.append(root.val)
  return values
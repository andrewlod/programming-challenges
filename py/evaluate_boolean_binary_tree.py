"""
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

Examples:
Input: root = [2,1,3,null,null,0,1]
Output: true

Input: root = [0]
Output: false

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import TreeNode

def evaluate_tree(root: Optional[TreeNode]) -> bool:
  if root.val == 0:
    return False
  
  if root.val == 1:
    return True

  if root.val == 2:
    return evaluate_tree(root.left) or evaluate_tree(root.right)

  return evaluate_tree(root.left) and evaluate_tree(root.right)
"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Examples:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Input: root = []
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

# Definition for a Node.
class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

def connect(root: 'Node') -> 'Node':
  if not root:
      return None
  
  nodes = [root]

  while nodes:
    next_nodes = []

    for i in range(len(nodes)-1):
      node = nodes[i]
      node.next = nodes[i+1]

      if node.left:
        next_nodes.append(node.left)

      if node.right:
        next_nodes.append(node.right)

    node = nodes[-1]
    node.next = None
    if node.left:
      next_nodes.append(node.left)

    if node.right:
      next_nodes.append(node.right)

    nodes = next_nodes

  return root
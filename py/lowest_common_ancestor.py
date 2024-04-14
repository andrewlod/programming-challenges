"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Examples:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5

Input: root = [1,2], p = 1, q = 2
Output: 1

Problem source: LeetCode

Usage: lowest_common_angestor.py <p> <q>
"""

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_ancestors(node: TreeNode, p: int):
    if node is None:
        return []

    if node.val == p:
        return [node]

    left_ancestors = find_ancestors(node.left, p)
    right_ancestors = find_ancestors(node.right, p)

    if left_ancestors:
        return left_ancestors + [node]
    elif right_ancestors:
        return right_ancestors + [node]

    return []

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    p_ancestors = find_ancestors(root, p.val)
    q_ancestors = find_ancestors(root, q.val)

    lowest = None

    while p_ancestors and q_ancestors:
        p_ancestor = p_ancestors.pop()
        q_ancestor = q_ancestors.pop()

        if p_ancestor == q_ancestor:
            lowest = p_ancestor
        else:
            break

    return lowest


if __name__ == "__main__":
  root = TreeNode(3)
  root.left = TreeNode(5)
  root.left.left = TreeNode(6)
  root.left.right = TreeNode(2)
  root.left.right.left = TreeNode(7)
  root.left.right.right = TreeNode(4)

  root.right = TreeNode(1)
  root.right.left = TreeNode(0)
  root.right.right = TreeNode(8)

  print(lowest_common_ancestor(root, TreeNode(int(sys.argv[1])), TreeNode(int(sys.argv[2]))))
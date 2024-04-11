"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area using the following steps:

If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

Examples:
Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]

Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]

Problem source: LeetCode

Usage: quad_tree.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
import sys

# Definition for a QuadTree node.
class Node:
  def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight

  def __repr__(self) -> str:
    return f"""
    Node(
      val: {self.val}
      isLeaf: {self.isLeaf}
      topLeft = {self.topLeft.__repr__()}
      topRight = {self.topRight.__repr__()}
      bottomLeft = {self.bottomLeft.__repr__()}
      bottomRight = {self.bottomRight.__repr__()}
    )
    """


def construct_grid(grid: List[List[Node]]) -> Node:
  if len(grid) == 1:
    return grid[0][0]

  new_grid = []
  for i in range(0, len(grid), 2):
    row = []

    for j in range(0, len(grid), 2):
      top_left = grid[i][j]
      top_right = grid[i][j+1]
      bot_left = grid[i+1][j]
      bot_right = grid[i+1][j+1]

      is_leaf = (top_left.isLeaf and top_right.isLeaf and bot_left.isLeaf and bot_right.isLeaf and
        top_left.val == top_right.val == bot_left.val == bot_right.val)

      val = top_left.val

      if is_leaf:
        top_left = None
        top_right = None
        bot_left = None
        bot_right = None

      row.append(Node(val, is_leaf, top_left, top_right, bot_left, bot_right))

    new_grid.append(row)

  return construct_grid(new_grid)


def construct(grid: List[List[int]]) -> Node:
  new_grid = [
    [Node(val, True, None, None, None, None) for val in row] for row in grid
  ]

  return construct_grid(new_grid)


if __name__ == "__main__":
  print(construct([
    [int(val) for val in row.split(',')] for row in sys.argv[1:]
  ]))
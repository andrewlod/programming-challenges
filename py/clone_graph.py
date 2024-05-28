"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Examples:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Input: adjList = [[]]
Output: [[]]

Input: adjList = []
Output: []

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

from typing import Optional, Dict

def clone(original: Optional['Node'], node: Optional['Node'], created: Dict[int, 'Node']):
  if len(original.neighbors) == len(node.neighbors):
    return

  for neighbor in original.neighbors:
    if neighbor.val in created:
      node.neighbors.append(created[neighbor.val])
    else:
      new_node = Node(neighbor.val)
      node.neighbors.append(new_node)
      created[neighbor.val] = new_node
      clone(neighbor, new_node, created)

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
  if not node:
    return None

  created = {}
  root_clone = Node(node.val)
  created[node.val] = root_clone
  clone(node, root_clone, created)

  return root_clone
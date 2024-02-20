"""
This script calculates what nodes are in a `k` distance from the node `x` in the following tree structure:

        1
       / \ 
      3   2
     / \   \ 
    4   6   7

Examples:
Input: 1,1
Output: [3,2]

Input: 1,2
Output: [4,6,7]

Input: 7 1
Output: [2]

Input: 7 2
Output: [1]

Input: 7 3
Output: [3]

Problem source: Interview Pen (https://www.youtube.com/watch?v=5dRTK-_Bzd0)

Usage: node_distance.py <x> <k>
"""
import sys

# Tree structure
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


def find_node(node: TreeNode, parents: list[TreeNode], x: int):
    """
    Finds the `x` node through depth-first search

    Parameters:
    node (TreeNode): Root node
    parents (list[TreeNode]): Empty list. When the `x` node is found, this list will have all of its hierarchical parents
    x (int): Goal node

    Returns:
    TreeNode: Node holding the value of `x`
    """
    if node is None:
        return None

    if node.val == x:
        return node
    
    parents_left = [node]
    found_left = find_node(node.left, parents_left, x)

    parents_right = [node]
    found_right = find_node(node.right, parents_right, x)

    if found_left:
        parents += parents_left
        return found_left
    
    if found_right:
        parents += parents_right
        return found_right

    return None


def find_k_nodes(node: TreeNode, visited: set[int], k: int):
    """
    Finds the k-distant nodes of x through depth-first search

    Parameters:
    node (TreeNode): Any node
    visited (set[int]): Set of already visited nodes
    k (int): Distance from the k-distant nodes

    Returns:
    list[TreeNode]: k-distant nodes of the starting node
    """
    if node is None or node.val in visited:
        return []

    visited.add(node.val)

    if k == 0:
        return [node]
    
    found_nodes = []
    found_nodes += find_k_nodes(node.left, visited, k-1)
    found_nodes += find_k_nodes(node.right, visited, k-1)

    return found_nodes


def node_distance(root: TreeNode, x: int, k: int):
    """
    Finds `x` and calculates the k-distant nodes.

    Parameters:
    root (TreeNode): Tree root
    x (int): Goal node
    k (int): Distance from `x`

    Returns:
    list[TreeNode]: k-distant nodes of `x`
    """
    parents = []
    results = []
    
    found_node = find_node(root, parents, x)
    visited = set()
    visited.add(found_node.val)

    if len(parents) >= k:
        node = parents[len(parents)-k]
        visited.add(node.val)
        results.append(node)

    iters = min(k-1, len(parents))
    for i in range(iters):
        found_nodes = find_k_nodes(parents[len(parents)-i-1], visited, k-i-1)

        results += found_nodes

    if found_node.left is not None:
        results += find_k_nodes(found_node.left, visited, k-1)

    if found_node.right is not None:
        results += find_k_nodes(found_node.right, visited, k-1)

    return results


def test(x: int, k: int):
    """
    Tests the algorithm.

    Parameters:
    x (int): Goal node
    k (int): Distance from `x`
    """
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(7)

    vals = node_distance(root, x, k)
    print([node.val for node in vals])


if __name__ == "__main__":
    test(int(sys.argv[1]), int(sys.argv[2]))
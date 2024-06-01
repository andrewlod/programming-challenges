from typing import List, Optional
from utils import TreeNode, read_int_array
import sys

def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
  def build_tree(arr: List[int], node: TreeNode):
    midpoint = len(arr)//2
    left = arr[:midpoint]
    right = arr[midpoint+1:]
    node.val = arr[midpoint]

    if left:
      node.left = TreeNode()
      build_tree(left, node.left)

    if right:
      node.right = TreeNode()
      build_tree(right, node.right)

  root = TreeNode()
  build_tree(nums, root)

  return root


if __name__ == '__main__':
  nums = read_int_array(sys.argv[1])
  root = sorted_array_to_bst(nums)
  print(root)
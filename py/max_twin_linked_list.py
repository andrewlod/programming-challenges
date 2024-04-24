"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Examples:
Input: head = [5,4,2,1]
Output: 6

Input: head = [4,2,2,3]
Output: 7

Input: head = [1,100000]
Output: 100001

Problem source: LeetCode

Usage: max_twin_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def pair_sum(head: Optional[ListNode]) -> int:
  node_list = []

  while head is not None:
    node_list.append(head.val)
    head = head.next

  max_twin = float('-inf')
  n = len(node_list)
  for i in range(n):
    max_twin = max(max_twin, node_list[i] + node_list[n-i-1])

  return max_twin
    

if __name__ == "__main__":
  print(pair_sum(read_int_linked_list(sys.argv[1])))
"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

Examples:
Input: head = [5,2,13,3,8]
Output: [13,8]

Input: head = [1,1,1,1]
Output: [1,1,1,1]

Problem source: LeetCode

Usage: remove_nodes_from_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def remove_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
  wrapper = ListNode(val=2147483647, next=head)
  stack = [wrapper]
  node = head

  while node:
    while stack[-1].val < node.val:
      stack.pop()

    stack[-1].next = node
    stack.append(node)
    node = node.next

  return wrapper.next


if __name__ == "__main__":
  print(remove_nodes(read_int_linked_list(sys.argv[1])))
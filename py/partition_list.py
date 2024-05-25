"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Examples:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [2,1], x = 2
Output: [1,2]

Problem source: LeetCode

Usage: partition_list.py <comma_separated_nums> <x>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
  higher_nodes = ListNode()
  last_higher_node = higher_nodes
  before_head = ListNode(next=head)
  node = before_head

  while node.next:
    if node.next.val >= x:
      temp = node.next.next
      last_higher_node.next = node.next
      last_higher_node = last_higher_node.next
      node.next.next = None
      node.next = temp
    else:
      node = node.next

  node.next = higher_nodes.next

  return before_head.next


if __name__ == "__main__":
  print(partition(read_int_linked_list(sys.argv[1]), int(sys.argv[2])))
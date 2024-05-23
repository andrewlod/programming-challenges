"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Examples:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Problem source: LeetCode

Usage: reverse_nodes_in_k_group.py <comma_separated_nums> <k>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  if k == 1:
    return head

  stack = []
  new_head = ListNode(next=head)
  start_value = new_head
  node = new_head.next

  while node:
    stack.append(node)

    if len(stack) == k:
      start_value.next = stack.pop()
      temp_node = start_value.next
      stack[0].next = node.next
      while stack:
        temp_node.next = stack.pop()
        temp_node = temp_node.next

      start_value = temp_node
      node = start_value.next
    else:
      node = node.next


  return new_head.next


def reverse_k_group_no_extra_space(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  if k == 1:
    return head

  new_head = ListNode(next=head)
  start_value = new_head
  previous = start_value
  node = new_head.next
  count = 0

  while node:
    temp = node
    node = node.next
    temp.next = previous

    if count < k-1:
      previous = temp
      count += 1
    else:
      next_start_value = start_value.next
      start_value.next = temp
      start_value = next_start_value
      start_value.next = node
      previous = start_value
      count = 0

  if count > 0:
    start_value.next.next = None
    node = previous
    previous = None
    while node:
      temp = node
      node = node.next
      temp.next = previous
      previous = temp

  return new_head.next


if __name__ == "__main__":
  print(reverse_k_group(read_int_linked_list(sys.argv[1]), int(sys.argv[2])))
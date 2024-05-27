"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Examples:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Problem source: LeetCode

Usage: remove_nth_node_linked_list.py <comma_separated_nums> <n>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  stack = []
  node = head

  while node:
    stack.append(node)
    node = node.next

  if len(stack) == n:
    return head.next

  stack[-n-1].next = stack[-n].next
  return head


def remove_nth_from_end_2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
  aux = ListNode(next=head)
  front = aux
  back = aux

  for _ in range(n+1):
    front = front.next

  while front:
    back = back.next
    front = front.next

  back.next = back.next.next

  return aux.next


if __name__ == "__main__":
  print(remove_nth_from_end_2(read_int_linked_list(sys.argv[1]), int(sys.argv[2])))
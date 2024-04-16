"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Examples:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Problem source: LeetCode

Usage: reverse_linked_list.py <comma_separated_numbers>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
  if head is None:
    return None

  tail = head
  previous = None

  while tail.next is not None:
    current = tail
    tail = tail.next
    current.next = previous
    previous = current


  tail.next = previous

  return tail


if __name__ == "__main__":
  print(reverse_list(read_int_linked_list(sys.argv[1])))
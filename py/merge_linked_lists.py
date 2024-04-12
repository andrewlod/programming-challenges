"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Examples:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]

Problem source: LeetCode

Usage: merge_linked_lists.py <comma_separated_values_1> <comma_separated_values_2>
"""

from typing import Optional
import sys

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  head = ListNode()
  merged = head

  while list1 is not None and list2 is not None:
    if list1.val > list2.val:
      merged.next = list2
      list2 = list2.next
    else:
      merged.next = list1
      list1 = list1.next

    merged = merged.next

  if list1 is not None:
    merged.next = list1

  if list2 is not None:
    merged.next = list2

  return head.next


if __name__ == "__main__":
  list1 = [int(val) for val in sys.argv[1].split(",")]
  list2 = [int(val) for val in sys.argv[2].split(",")]

  head = ListNode()
  current = head
  for val in list1:

    current.next = ListNode(val)
    current = current.next

  linked_list_1 = head.next

  head = ListNode()
  current = head
  for val in list2:

    current.next = ListNode(val)
    current = current.next

  linked_list_2 = head.next

  merged = merge_two_lists(linked_list_1, linked_list_2)

  while merged is not None:
    print(merged.val, end=" ")
    merged = merged.next
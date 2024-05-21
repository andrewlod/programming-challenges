"""
Given the head of a linked list, return the list after sorting it in ascending order.

Examples:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Input: head = []
Output: []

Problem source: LeetCode

Usage: sort_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  values = []

  while head:
    values.append(head.val)
    head = head.next

  values.sort()
  new_head = ListNode(val=values[0])
  node = new_head

  for i in range(1, len(values)):
    node.next = ListNode(val=values[i])
    node = node.next

  return new_head


def divide_and_conquer(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  slow = head
  fast = head

  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

  second_list = slow.next
  slow.next = None

  merged_first = divide_and_conquer(head)
  merged_second = divide_and_conquer(second_list)

  head = None
  first = None
  second = None
  if (merged_first or not merged_second) and merged_first.val < merged_second.val:
    head = merged_first
    first = merged_first
    second = merged_second
  else:
    head = merged_second
    first = merged_second
    second = merged_first

  while second:
    if not first.next:
      first.next = second
      break

    if second.val < first.next.val:
      temp_1 = first.next
      temp_2 = second.next
      first.next = second
      second.next = temp_1
      second = temp_2
    else:
      first = first.next

  return head

def sort_list_2(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  return divide_and_conquer(head)


if __name__ == "__main__":
  print(sort_list(read_int_linked_list(sys.argv[1])))
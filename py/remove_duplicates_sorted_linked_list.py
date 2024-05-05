"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Examples:
Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Problem source: LeetCode

Usage: remove_duplicates_sorted_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head:
    return None

  ptr = head
  while ptr.next:
    if ptr.next.val == ptr.val:
      ptr.next = ptr.next.next
    else:
      ptr = ptr.next

  return head


if __name__ == "__main__":
  print(delete_duplicates(read_int_linked_list(sys.argv[1])))
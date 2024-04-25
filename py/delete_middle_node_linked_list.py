"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Examples:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]

Input: head = [1,2,3,4]
Output: [1,2,4]

Input: head = [2,1]
Output: [2]

Problem source: LeetCode

Usage: delete_middle_node_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head.next:
    return None

  slow = head
  fast = head.next

  while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

  slow.next = slow.next.next

  return head


if __name__ == "__main__":
  print(delete_middle(read_int_linked_list(sys.argv[1])))
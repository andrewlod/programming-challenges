"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Examples:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Problem source: LeetCode

Usage: add_even_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  odd = head
  first_even = head.next
  current_even = first_even

  while current_even and current_even.next:
    odd.next = current_even.next
    current_even.next = current_even.next.next

    odd = odd.next
    current_even = current_even.next

  odd.next = first_even

  return head


if __name__ == "__main__":
  print(odd_even_list(read_int_linked_list(sys.argv[1])))
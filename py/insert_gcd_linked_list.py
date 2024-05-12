"""
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Examples:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]

Input: head = [7]
Output: [7]

Problem source: LeetCode

Usage: insert_gcd_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
from math import gcd
import sys

def insert_greatest_common_divisors(head: Optional[ListNode]) -> Optional[ListNode]:
  if not head or not head.next:
    return head

  first = head.val
  second = head.next.val
  head.next = ListNode(val=gcd(first, second), next=head.next)
  fast = head.next.next

  while fast.next:
    first = fast.val
    second = fast.next.val
    fast.next = ListNode(val=gcd(first, second), next=fast.next)
    fast = fast.next.next

  return head


if __name__ == "__main__":
  print(insert_greatest_common_divisors(read_int_linked_list(sys.argv[1])))
"""
Given the head of a linked list, rotate the list to the right by k places.

Examples:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Problem source: LeetCode

Usage: rotate_linked_list.py <comma_separated_nums> <k>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
  if not head or not head.next or k == 0:
    return head

  count = 0
  k_pointer = head
  while k_pointer and count < k:
    k_pointer = k_pointer.next
    count += 1

  if not k_pointer:
    k %= count

    if k == 0:
      return head
    
    k_pointer = head
    count = 0
    while count < k:
      k_pointer = k_pointer.next
      count += 1

  node = head
  while k_pointer.next:
    node = node.next
    k_pointer = k_pointer.next

  new_head = node.next
  node.next = None
  k_pointer.next = head
  return new_head

if __name__ == "__main__":
  print(rotate_right(read_int_linked_list(sys.argv[1]), int(sys.argv[2])))
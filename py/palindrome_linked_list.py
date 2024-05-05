"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Examples:
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

Problem source: LeetCode

Usage: palindrome_linked_list.py <comma_separated_nums>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def is_palindrome(head: Optional[ListNode]) -> bool:
  if not head.next:
    return True

  previous = None
  slow = head
  fast = head

  while fast.next and fast.next.next:
    temp = slow
    slow = slow.next
    fast = fast.next.next
    temp.next = previous
    previous = temp

  first_half_ptr = slow
  second_half_ptr = slow.next
  if fast.next:
    first_half_ptr.next = previous
  else:
    first_half_ptr = previous

  while first_half_ptr and second_half_ptr:
    if first_half_ptr.val != second_half_ptr.val:
      return False

    first_half_ptr = first_half_ptr.next
    second_half_ptr = second_half_ptr.next

  return (first_half_ptr is None and second_half_ptr is None)


if __name__ == "__main__":
  print(is_palindrome(read_int_linked_list(sys.argv[1])))
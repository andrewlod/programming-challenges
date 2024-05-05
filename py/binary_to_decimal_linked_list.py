"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Examples:
Input: head = [1,0,1]
Output: 5

Input: head = [0]
Output: 0

Problem source: LeetCode

Usage: binary_to_decimal_linked_list.py <comma_separated_nums>
"""

from utils import ListNode, read_int_linked_list
import sys

def get_decimal_value(head: ListNode) -> int:
  number = 0
  while head:
    number <<= 1
    number += head.val
    head = head.next

  return number


if __name__ == '__main__':
  print(get_decimal_value(read_int_linked_list(sys.argv[1])))
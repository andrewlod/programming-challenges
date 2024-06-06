"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Input: l1 = [0], l2 = [0]
Output: [0]

Problem source: LeetCode

Usage: add_two_linked_lists.py <comma_separated_nums1> <comma_separated_nums2>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  stack1 = []
  stack2 = []

  node1 = l1
  while node1:
    stack1.append(node1)
    node1 = node1.next

  node2 = l2
  while node2:
    stack2.append(node2)
    node2 = node2.next

  largest_stack = None
  smallest_stack = None
  target_node = None
  if len(stack1) > len(stack2):
    largest_stack = stack1
    smallest_stack = stack2
    target_node = l1
  else:
    largest_stack = stack2
    smallest_stack = stack1
    target_node = l2

  carry_over = 0
  while largest_stack and smallest_stack:
    node1 = largest_stack.pop()
    node2 = smallest_stack.pop()

    node_sum = node1.val + node2.val + carry_over
    carry_over = node_sum // 10
    node1.val = node_sum % 10

  while largest_stack and carry_over > 0:
    node1 = largest_stack.pop()

    node_sum = node1.val + carry_over
    carry_over = node_sum // 10
    node1.val = node_sum % 10

  if carry_over > 0:
    target_node = ListNode(val=carry_over, next=target_node)

  return target_node


if __name__ == '__main__':
  l1 = read_int_linked_list(sys.argv[1])
  l2 = read_int_linked_list(sys.argv[2])
  print(add_two_numbers(l1, l2))
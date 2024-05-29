"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Examples:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

Problem source: LeetCode

Usage: reverse_linked_list_2.py <comma_separated_nums> <idx_start> <idx_end>
"""

from typing import Optional
from utils import ListNode, read_int_linked_list
import sys

def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
  if left == right:
    return head

  new_head = ListNode(val=-1000, next=head)
  starting_node = new_head
  previous = starting_node
  node = new_head
  reversing = False
  i = -1

  while node.next:
    i += 1
    if i + 1 == left:
      reversing = True
      starting_node = node
      previous = node
      node = node.next
      continue

    if i == right:
      after = node.next
      end = starting_node.next
      node.next = previous
      starting_node.next = node
      end.next = after
      return new_head.next

    if reversing:
      temp = node
      node = node.next
      temp.next = previous
      previous = temp
    else:
      previous = node
      node = node.next

  after = node.next
  end = starting_node.next
  node.next = previous
  starting_node.next = node
  end.next = None

  return new_head.next


if __name__ == "__main__":
  print(reverse_between(read_int_linked_list(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
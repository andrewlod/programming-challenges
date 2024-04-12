"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Examples:
Input: head = [3,2,0,-4], pos = 1
Output: true

Input: head = [1,2], pos = 0
Output: true

Input: head = [1], pos = -1
Output: false

Problem source: LeetCode

Usage: linked_list_cycle.py <val1>,<next_idx_1> <val2>,<next_idx_2> ...
"""

from typing import Optional
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    current_node = head

    while current_node is not None:
        current_node.seen = True
        current_node = current_node.next

        if hasattr(current_node, 'seen'):
            return True

    return False


def has_cycle_2(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is not None and slow is fast:
            return True

    return False


if __name__ == "__main__":
  items = [item.split(",") for item in sys.argv[1:]]
  nodes = [ListNode(int(val)) for val, _ in items]

  for node, item in zip(nodes, items):
    node.next = None if int(item[1]) == -1 else nodes[int(item[1])]

  print(has_cycle_2(nodes[0]))
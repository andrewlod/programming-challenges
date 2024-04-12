"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Examples:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Input: lists = []
Output: []

Input: lists = [[]]
Output: []

Problem source: LeetCode

Usage: merge_k_sorted_lists.py <comma_separated_values_1> <comma_separated_values_2> ...
"""

from typing import List, Optional
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_min_idx(lists: List[Optional[ListNode]]) -> int:
    min_idx = 0
    
    for i, item in enumerate(lists[1:]):
        if item is None:
            continue

        min_item = lists[min_idx]
        if min_item is None or item.val < min_item.val:
            min_idx = i + 1

    if lists[min_idx] is None:
        return -1

    return min_idx


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None

    min_idx = get_min_idx(lists)
    head = ListNode()
    merged = head

    while min_idx != -1:
        min_item = lists[min_idx]

        merged.next = min_item
        merged = merged.next
        lists[min_idx] = lists[min_idx].next
        
        min_idx = get_min_idx(lists)

    return head.next


if __name__ == "__main__":
  lists = [[int(val) for val in item.split(",")] for item in sys.argv[1:]]
  linked_lists = []

  for item in lists:
    head = ListNode()
    current = head

    for val in item:
      current.next = ListNode(val)
      current = current.next

    linked_lists.append(head.next)

  merged = merge_k_lists(linked_lists)

  while merged is not None:
    print(merged.val, end=" ")
    merged = merged.next
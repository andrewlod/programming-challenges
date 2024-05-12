"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Examples:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]

Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]

Problem source: LeetCode

Usage: merge_nodes_between_zeros.py <comma_separated_nums>
"""

from typing import Optional, Optional
from utils import ListNode, read_int_linked_list
import sys

def merge_nodes(head: Optional[ListNode]) -> Optional[ListNode]:
  merged_head = ListNode(val = 0)
  merged_node = merged_head

  node = head

  while node.next.next:
    node = node.next
    if node.val == 0:
      merged_node.next = ListNode(val = 0)
      merged_node = merged_node.next
    else:
      merged_node.val += node.val

  return merged_head


if __name__ == "__main__":
  print(merge_nodes(read_int_linked_list(sys.argv[1])))
"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Examples:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]

Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]

Problem source: LeetCode

Usage: merge_in_between_linked_lists.py <comma_separated_nums1> <a> <b> <comma_separated_nums2>
"""

from utils import ListNode, read_int_linked_list
import sys

def merge_in_between(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
  remove_start = list1
  remove_end = list1
  list2_end = list2

  while list2_end.next:
    list2_end = list2_end.next

  idx = 1
  while idx < a:
    remove_start = remove_start.next
    idx += 1

  remove_end = remove_start
  while idx <= b + 1:
    remove_end = remove_end.next
    idx += 1

  remove_start.next = list2
  list2_end.next = remove_end


if __name__ == "__main__":
  list1 = read_int_linked_list(sys.argv[1])
  a = int(sys.argv[2])
  b = int(sys.argv[3])
  list2 = read_int_linked_list(sys.argv[4])
  print(merge_in_between(list1, a, b, list2))
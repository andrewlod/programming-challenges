"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Examples:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import Optional
from utils import ListNode

def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  viewed_nodes = {}

  while headA and headB:
    if id(headA) in viewed_nodes:
      return viewed_nodes[id(headA)]
        
    viewed_nodes[id(headA)] = headA
    headA = headA.next

    if id(headB) in viewed_nodes:
      return viewed_nodes[id(headB)]

    viewed_nodes[id(headB)] = headB
    headB = headB.next

  while headA:
    if id(headA) in viewed_nodes:
      return viewed_nodes[id(headA)]
      
    headA = headA.next

  while headB:
    if id(headB) in viewed_nodes:
      return viewed_nodes[id(headB)]

    headB = headB.next

  return None

def get_intersection_node_2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  ptr_a = headA
  ptr_b = headB

  while id(ptr_a) != id(ptr_b):
    if not ptr_a:
      ptr_a = headB
    else:
      ptr_a = ptr_a.next

    if not ptr_b:
      ptr_b = headA
    else:
      ptr_b = ptr_b.next

  return ptr_a
from typing import List, Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __repr__(self) -> str:
    values = []
    current = self
    while current is not None:
      values.append(str(current.val))
      current = current.next

    return "[" + ", ".join(values) + "]"


def read_int_array(input: str) -> List[int]:
  return [int(val) for val in input.split(",")]


def read_str_array(input: str) -> List[int]:
  return input.split(",")


def read_int_linked_list(input: str) -> Optional[ListNode]:
  head = ListNode()
  current = head

  for val in input.split(","):
      current.next = ListNode(int(val))
      current = current.next

  return head.next


def read_int_matrix(input: str) -> List[List[int]]:
  return [
    [int(val) for val in item.split(",")] for item in input.split(" ")
  ]


def read_str_matrix(input: str) -> List[List[str]]:
  return [
    [val for val in item] for item in input.split(",")
  ]
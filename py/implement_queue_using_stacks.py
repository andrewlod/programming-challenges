"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Examples:
Input
  ["MyQueue", "push", "push", "peek", "pop", "empty"]
  [[], [1], [2], [], [], []]
Output
  [null, null, null, 1, 1, false]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class MyQueue:

  def __init__(self):
    self.ordered_stack = []
    self.original_stack = []

  def reorder(self):
    if len(self.ordered_stack) > 0:
      return

    while len(self.original_stack) > 0:
      self.ordered_stack.append(self.original_stack.pop())

  def push(self, x: int) -> None:
    self.original_stack.append(x)

  def pop(self) -> int:
    self.reorder()
    return self.ordered_stack.pop()

  def peek(self) -> int:
    self.reorder()
    return self.ordered_stack[-1]

  def empty(self) -> bool:
    return (len(self.original_stack) + len(self.ordered_stack)) == 0
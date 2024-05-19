"""
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

Examples:
Input
  ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
  [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
Output
  [null,null,null,2,null,null,null,null,null,103,202,201,-1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class CustomStack:

  def __init__(self, maxSize: int):
    self.max_size = maxSize
    self.stack = []

  def push(self, x: int) -> None:
    if len(self.stack) < self.max_size:
      self.stack.append(x)

  def pop(self) -> int:
    if len(self.stack) == 0:
      return -1

    return self.stack.pop()

  def increment(self, k: int, val: int) -> None:
    for i in range(min(k, len(self.stack))):
      self.stack[i] += val
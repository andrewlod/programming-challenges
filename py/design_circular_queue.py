"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Examples:
Input
  ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
  [[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
  [null, true, true, true, false, 2, true, true, true, 4]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class MyCircularDeque:

  def __init__(self, k: int):
    self.start = 0
    self.size = 0
    self.k = k
    self.values = [-1] * k

  def insertFront(self, value: int) -> bool:
    if self.isFull():
      return False

    self.start = (self.start -1) % self.k
    self.size += 1
    self.values[self.start] = value
    
    return True

  def insertLast(self, value: int) -> bool:
    if self.isFull():
      return False
    self.size += 1
    self.values[(self.start + self.size-1) % self.k] = value
    
    return True

  def deleteFront(self) -> bool:
    if self.isEmpty():
      return False
    
    self.values[self.start] = -1
    self.start = (self.start + 1) % self.k
    self.size -= 1
    
    return True

  def deleteLast(self) -> bool:
    if self.isEmpty():
      return False
    
    self.values[(self.start + self.size-1) % self.k] = -1
    self.size -= 1
    
    return True

  def getFront(self) -> int:
    if self.isEmpty():
      return -1

  def getRear(self) -> int:
    if self.isEmpty():
      return -1

    return self.values[(self.start + self.size-1) % self.k]

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size == self.k
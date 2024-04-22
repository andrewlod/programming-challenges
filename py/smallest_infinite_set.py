"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Examples:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Problem source: LeetCode

Usage:  NOT YET IMPLEMENTED
"""

from heapq import heappush, heappop

# First implementation: Just use set to track the removed numbers
class SmallestInfiniteSet1:

  def __init__(self):
    self.removed = set()
    self.smallest = 1

  def pop_smallest(self) -> int:
    smallest = self.smallest
    self.removed.add(self.smallest)

    while self.smallest in self.removed:
      self.smallest += 1

    return smallest

  def addBack(self, num: int) -> None:
    if num not in self.removed:
      return

    if num < self.smallest:
      self.smallest = num

    self.removed.remove(num)

# Second implementation: Using heap to track the re-added nums
class SmallestInfiniteSet2:

  def __init__(self):
    self.re_added = []
    self.popped = set()
    self.smallest = 1

  def pop_smallest(self) -> int:
    if self.re_added:
      num = heappop(self.re_added)
      self.popped.add(num)
      return num
    else:
      smallest = self.smallest
      self.smallest += 1
      self.popped.add(smallest)
      return smallest

  def addBack(self, num: int) -> None:
      if num not in self.popped:
        return

      heappush(self.re_added, num)
      self.popped.remove(num)


if __name__ == "__main__":
  pass
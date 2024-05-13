"""
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Examples:
Input
  ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
  [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
Output
  [null,null,null,null,null,null,20,40,0,null,32]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class ProductOfNumbers:

  def __init__(self):
    self.values = [0]
    self.zero_idx = -1

  def add(self, num: int) -> None:
    if num == 0:
      self.zero_idx = len(self.values)-1
      self.values.append(0)
    else:
      self.values.append((self.values[-1] if self.values[-1] else 1) * num)

  def getProduct(self, k: int) -> int:
    if len(self.values) - k - 1 <= self.zero_idx:
      return 0
    
    if self.values[-k-1] == 0:
      return self.values[-1]

    return self.values[-1] // self.values[-k-1]
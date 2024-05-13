"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Examples:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
  def isInteger(self) -> bool:
    """
    @return True if this NestedInteger holds a single integer, rather than a nested list.
    """

  def getInteger(self) -> int:
    """
    @return the single integer that this NestedInteger holds, if it holds a single integer
    Return None if this NestedInteger holds a nested list
    """

  def getList(self) -> List[NestedInteger]:
    """
    @return the nested list that this NestedInteger holds, if it holds a nested list
    Return None if this NestedInteger holds a single integer
    """

class NestedIterator:
  def flatten(self, nested_list: List[NestedInteger]) -> List[int]:
    integers = []
    for nested in nested_list:
      if nested.isInteger():
        integers.append(nested.getInteger())
      else:
        integers += self.flatten(nested.getList())

    return integers

  def __init__(self, nestedList: List[NestedInteger]):
    self.flat_list = self.flatten(nestedList)
    self.idx = 0
  
  def next(self) -> int:
    item = self.flat_list[self.idx]
    self.idx += 1
    return item
  
  def hasNext(self) -> bool:
    return self.idx < len(self.flat_list)
"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Examples:
Input
  ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
  [[], [1], [2], [2], [], [1], [2], []]
Output
  [null, true, false, true, 2, true, false, 2]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

import random

class RandomizedSet:

  def __init__(self):
    self.items = set()
    self.items_arr = []
    self.removed = set()

  def insert(self, val: int) -> bool:
    if val in self.items:
      return False
    
    self.items.add(val)
    if val in self.removed:
      self.removed.remove(val)
    else:
      self.items_arr.append(val)

    return True

  def remove(self, val: int) -> bool:
    if val not in self.items:
      return False
    
    self.items.remove(val)
    self.removed.add(val)
    return True

  def getRandom(self) -> int:
    num = random.choice(self.items_arr)
    while num in self.removed:
      num = random.choice(self.items_arr)

    return num


class RandomizedSet2:

  def __init__(self):
    self.items = []
    self.indices = {}

  def insert(self, val: int) -> bool:
    if val in self.items:
      return False
    
    self.indices[val] = len(self.items)
    self.items.append(val)

    return True

  def remove(self, val: int) -> bool:
    if val not in self.items:
      return False
    
    idx = self.indices[val]
    last_element = self.items[-1]
    self.items[idx] = last_element
    self.items.pop()
    self.indices[last_element] = idx
    return True

  def getRandom(self) -> int:
    return random.choice(self.items)
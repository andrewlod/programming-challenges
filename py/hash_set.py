"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Examples:
Input:
  ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
  [[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output: 
  [null, null, null, true, false, null, true, null, false]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class MyHashSet:

  def __init__(self):
    self.table_size = 1024
    self.hash_table = [[] for _ in range(self.table_size)]

  def add(self, key: int) -> None:
    arr = self.hash_table[key%self.table_size]
    if key in arr:
      return
    
    arr.append(key)
      

  def remove(self, key: int) -> None:
    arr = self.hash_table[key%self.table_size]
    if key not in arr:
      return
    
    arr.remove(key)
      

  def contains(self, key: int) -> bool:
    return key in self.hash_table[key%self.table_size]
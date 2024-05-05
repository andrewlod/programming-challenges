"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Examples:
Input:
  ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
  [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output:
  [null, null, null, 1, -1, null, 1, null, -1]

Problem source: LeetCode

Usage: NOT YET IMPLEMENTED
"""

class MyHashMap:

  def __init__(self):
    self.table_size = 1024
    self.hash_table = [[] for _ in range(self.table_size)]

  def put(self, key: int, value: int) -> None:
    arr = self.hash_table[key%self.table_size]

    for i, item in enumerate(arr):
      if item[0] == key:
        arr[i] = (key, value)
        return

    arr.append((key, value))

  def get(self, key: int) -> int:
    arr = self.hash_table[key%self.table_size]

    for item in arr:
      if item[0] == key:
        return item[1]

    return -1

  def remove(self, key: int) -> None:
    arr = self.hash_table[key%self.table_size]

    to_remove = None
    for item in arr:
      if item[0] == key:
        to_remove = item

    if to_remove:
      arr.remove(to_remove)
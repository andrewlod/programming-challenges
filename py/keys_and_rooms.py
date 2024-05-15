"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Examples:
Input: rooms = [[1],[2],[3],[]]
Output: true

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false

Problem source: LeetCode

Usage: keys_and_rooms.py "key_0,key_1,key_2... key_0,key_1... ..."
"""

from typing import List
from utils import read_int_matrix
import sys

def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
  n = len(rooms)
  visited = set([])

  to_visit = [0]
  while to_visit:
    next_to_visit = []

    for door in to_visit:
      if door in visited:
        continue

      visited.add(door)
      next_to_visit += rooms[door]

    to_visit = next_to_visit

  return len(visited) == n


if __name__ == "__main__":
  print(can_visit_all_rooms(read_int_matrix(sys.argv[1])))
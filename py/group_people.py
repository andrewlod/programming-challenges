"""
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

Examples:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

Problem source: LeetCode

Usage: group_people.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def group_the_people(group_sizes: List[int]) -> List[List[int]]:
  groups = {}

  for i, size in enumerate(group_sizes):
    if size not in groups:
      groups[size] = [[]]

    found_group = False
    for group in groups[size]:
      if len(group) < size:
        group.append(i)
        found_group = True
        break

    if not found_group:
      groups[size].append([i])
  
  return [group for group_list in groups.values() for group in group_list]


if __name__ == "__main__":
  print(group_the_people(read_int_array(sys.argv[1])))
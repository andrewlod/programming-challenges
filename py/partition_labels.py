"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Examples:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Input: s = "eccbbbbdec"
Output: [10]

Problem source: LeetCode

Usage: partition_labels.py <s>
"""

from typing import List
import sys

def partition_labels(s: str) -> List[int]:
  n = len(s)

  result = []
  last_idx = -1
  partition_chars = set([s[0]])

  while last_idx < n-1:
    temp_partition_chars = set()
    start_idx = last_idx
    for i in range(last_idx+1, n):
      char = s[i]
      if char in partition_chars:
        last_idx = i
        partition_chars.update(temp_partition_chars)
        temp_partition_chars = set()
      else:
        temp_partition_chars.add(char)

    result.append(last_idx - start_idx)
    if last_idx < n-1:
      partition_chars = set([s[last_idx+1]])

  return result


if __name__ == "__main__":
  print(partition_labels(sys.argv[1]))
"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Examples:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]

Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]

Problem source: LeetCode

Usage: find_prefix_common_of_arrays.py <comma_separated_A> <comma_separated_B>
"""

from typing import List
from utils import read_int_array
import sys

def find_the_prefix_common_array(A: List[int], B: List[int]) -> List[int]:
  set_a = set()
  set_b = set()

  counts = []
  current_count = 0
  for a, b in zip(A, B):
    if a == b:
      current_count += 1
      counts.append(current_count)
      continue

    if a in set_b:
      set_b.remove(a)
      current_count += 1
    else:
      set_a.add(a)

    if b in set_a:
      set_a.remove(b)
      current_count += 1
    else:
      set_b.add(b)

    counts.append(current_count)

  return counts


if __name__ == "__main__":
  print(find_the_prefix_common_array(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Examples:
Input: citations = [3,0,6,1,5]
Output: 3

Input: citations = [1,3,1]
Output: 1

Problem source: LeetCode

Usage: h_index.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def h_index(citations: List[int]) -> int:
  sorted_citations = sorted(citations)
  n = len(citations)

  best = 1
  for i, num in enumerate(sorted_citations):
    if n - i >= num:
      best = num
    else:
      best = max(n-i, best)
      return best

  return best


if __name__ == "__main__":
  print(h_index(read_int_array(sys.argv[1])))
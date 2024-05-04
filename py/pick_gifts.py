"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

Examples:
Input: gifts = [25,64,9,4,100], k = 4
Output: 29

Input: gifts = [1,1,1,1], k = 4
Output: 4

Problem source: LeetCode

Usage: pick_gifts.py <comma_separated_nums> <k>
"""

from heapq import _heapify_max, _heappop_max, _siftdown_max
from math import floor, sqrt
from typing import List
from utils import read_int_array
import sys

def heappush_max(max_heap, item): 
  max_heap.append(item)
  _siftdown_max(max_heap, 0, len(max_heap)-1)

def pick_gifts(gifts: List[int], k: int) -> int:
  _heapify_max(gifts)
  for i in range(k):
    gift = _heappop_max(gifts)
    heappush_max(gifts, floor(sqrt(gift)))

  return sum(gifts)


if __name__ == "__main__":
  print(pick_gifts(read_int_array(sys.argv[1]), int(sys.argv[2])))
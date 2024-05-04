"""
You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

Examples:
Input: amount = [1,4,2]
Output: 4

Input: amount = [5,4,4]
Output: 7

Input: amount = [5,0,0]
Output: 5

Problem source: LeetCode

Usage: fill_cups.py <num1,num2,num3>
"""

from heapq import _heapify_max, _heappop_max, _siftdown_max
from typing import List
from utils import read_int_array
import sys

def heappush_max(max_heap, item): 
  max_heap.append(item)
  _siftdown_max(max_heap, 0, len(max_heap)-1)


def fill_cups(amount: List[int]) -> int:
  _heapify_max(amount)

  seconds = 0
  empty = False
  while True:
    max_element = _heappop_max(amount)
    if max_element == 0:
      break

    second_max_element = _heappop_max(amount)
    if second_max_element == 0:
      return seconds + max_element

    heappush_max(amount, second_max_element-1)
    heappush_max(amount, max_element-1)
    seconds += 1

  return seconds


if __name__ == "__main__":
  print(fill_cups(read_int_array(sys.argv[1])))
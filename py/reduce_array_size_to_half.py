"""
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Examples:
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2

Input: arr = [7,7,7,7,7,7]
Output: 1

Problem source: LeetCode

Usage: reduce_array_size_to_half.py <comma_separated_nums>
"""

from heapq import heapify, heappop
from typing import List
from utils import read_int_array
import sys

def min_set_size(arr: List[int]) -> int:
  frequencies = {}

  for num in arr:
    if num not in frequencies:
      frequencies[num] = 1
    else:
      frequencies[num] += 1

  frequency_heap = [-num for num in frequencies.values()]
  heapify(frequency_heap)
  removed = 0
  count = 0
  while removed < len(arr) / 2:
    removed -= heappop(frequency_heap)
    count += 1

  return count


if __name__ == '__main__':
  print(min_set_size(read_int_array(sys.argv[1])))
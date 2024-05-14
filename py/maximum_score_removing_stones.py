"""
You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a, b, and c, return the maximum score you can get.

Examples:
Input: a = 2, b = 4, c = 6
Output: 6

Input: a = 4, b = 4, c = 6
Output: 7

Input: a = 1, b = 8, c = 8
Output: 8

Problem source: LeetCode

Usage: maximum_score_removing_stones.py <a> <b> <c>
"""

from heapq import heapify, heappop, heappush
import sys

def maximum_score(a: int, b: int, c: int) -> int:
  values = [-a, -b, -c]
  heapify(values)

  count = 0
  a = heappop(values)
  b = heappop(values)

  while a < 0 and b < 0:
    count += 1
    heappush(values, a+1)
    heappush(values, b+1)
    
    a = heappop(values)
    b = heappop(values)

  return count


if __name__ == '__main__':
  print(maximum_score(
    int(sys.argv[1]),
    int(sys.argv[2]),
    int(sys.argv[3])
  ))
"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Examples:
Input: ratings = [1,0,2]
Output: 5

Input: ratings = [1,2,2]
Output: 4

Problem source: LeetCode

Usage: candy.py <ratings>
"""

from typing import List
from utils import read_int_array
import sys

def candy(ratings: List[int]) -> int:
  n = len(ratings)
  candies = [1] * n

  for i in range(1, n):
    if ratings[i-1] < ratings[i]:
      candies[i] = candies[i-1] + 1

  for i in range(n-2, -1, -1):
    if ratings[i+1] < ratings[i]:
      candies[i] = max(candies[i], candies[i+1] + 1)

  return sum(candies)


if __name__ == "__main__":
  print(candy(read_int_array(sys.argv[1])))
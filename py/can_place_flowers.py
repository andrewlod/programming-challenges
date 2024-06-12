"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Examples:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Problem source: LeetCode

Usage: can_place_flowers.py <comma_separated_nums> <n>
"""

from typing import List
from utils import read_int_array
import sys

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
  if n == 0:
    return True
  
  count = 0

  for i, plot in enumerate(flowerbed):
    if plot == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
      count += 1
      flowerbed[i] = 1

      if count >= n:
        return True

  return False


if __name__ == '__main__':
  print(can_place_flowers(read_int_array(sys.argv[1]), int(sys.argv[2])))
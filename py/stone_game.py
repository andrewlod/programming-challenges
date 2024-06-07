"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Examples:
Input: piles = [5,3,4,5]
Output: true

Input: piles = [3,7,2,3]
Output: true

Problem source: LeetCode

Usage: stone_game.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def stone_game(piles: List[int]) -> bool:
  return True


if __name__ == '__main__':
  print(stone_game(read_int_array(sys.argv[1])))
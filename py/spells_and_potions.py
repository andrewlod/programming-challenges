"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Examples:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]

Problem source: LeetCode

Usage: spells_and_potions.py <comma_separated_spells> <comma_separated_potions> <success>
"""

from typing import List
from utils import read_int_array
import sys

def binary_search_potions(spell: int, potions: List[int], success: int):
  l = 0
  r = len(potions)

  while l < r:
    midpoint = (l + r) // 2

    if potions[midpoint] * spell < success:
      l = midpoint + 1
    else:
      r = midpoint

  return l

def successful_pairs(spells: List[int], potions: List[int], success: int) -> List[int]:
  successful_spells = [0] * len(spells)
  potions.sort()
  m = len(potions)

  for i, spell in enumerate(spells):
    successful_spells[i] = m - binary_search_potions(spell, potions, success)

  return successful_spells


if __name__ == "__main__":
  print(successful_pairs(
    read_int_array(sys.argv[1]),
    read_int_array(sys.argv[2]),
    int(sys.argv[3]))
  )
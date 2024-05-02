"""
You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise.

Examples:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true

Input: deck = [1,1,1,2,2,2,3,3]
Output: false

Problem source: LeetCode

Usage: x_kind_deck_of_cards.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_common_divisors(num: int) -> List[int]:
  divisors = []
  if num % 2 == 0:
    divisors.append(2)

  for i in range(3, num//3+1, 2):
    if num % i == 0:
      divisors.append(i)

  divisors.append(num)
  return divisors

def has_groups_size_x(deck: List[int]) -> bool:
  freqs = {}

  for num in deck:
    if num not in freqs:
      freqs[num] = 1
    else:
      freqs[num] += 1

  unique_freqs = set(freqs.values())
  divisors = find_common_divisors(min(unique_freqs))

  found_combination = False
  for divisor in divisors:
    possible = True
    for num in unique_freqs:
      if num % divisor != 0:
        possible = False

    if possible:
      found_combination = True
      break

  return found_combination and 1 not in unique_freqs


if __name__ == "__main__":
  print(has_groups_size_x(read_int_array(sys.argv[1])))
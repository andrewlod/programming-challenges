"""
You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.

Examples:
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]

Input: deck = [1,1000]
Output: [1,1000]

Problem source: LeetCode

Usage: reveal_cards_increasing_order.py <comma_separated_nums>
"""

from typing import List
from collections import deque
from utils import read_int_array
import sys

def deck_revealed_increasing(deck: List[int]) -> List[int]:
  n = len(deck)
  sorted_deck = sorted(deck)

  arr = [0] * n
  deck_ptr = 0
  indexes = deque([i for i in range(n)])

  while indexes:
    arr[indexes.popleft()] = sorted_deck[deck_ptr]
    if indexes:
      indexes.append(indexes.popleft())
    deck_ptr += 1

  return arr


if __name__ == "__main__":
  print(deck_revealed_increasing(read_int_array(sys.argv[1])))
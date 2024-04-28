"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

Examples:
Input: n = 2
Output: true

Input: n = 3
Output: false

Problem source: LeetCode

Usage: divisor_game.py <n>
"""

import sys

def divisor_game(n: int) -> bool:
  return n % 2 == 0


if __name__ == '__main__':
  print(divisor_game(int(sys.argv[1])))
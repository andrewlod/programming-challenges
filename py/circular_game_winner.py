"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

Examples:
Input: n = 5, k = 2
Output: 3

Input: n = 6, k = 5
Output: 1

Problem source: LeetCode

Usage: circular_game_winner.py <n> <k>
"""

from collections import deque
import sys

def find_the_winner(n: int, k: int) -> int:
  people = deque([i+1 for i in range(n)])

  while len(people) > 1:
    for _ in range((k-1) % len(people)):
      people.append(people.popleft())

    people.popleft()

  return people.popleft()


if __name__ == '__main__':
  print(find_the_winner(int(sys.argv[1]), int(sys.argv[2])))
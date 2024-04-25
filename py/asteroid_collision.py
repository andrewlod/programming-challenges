"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Examples:
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [10,2,-5]
Output: [10]

Problem source: LeetCode

Usage: asteroid_collision.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def asteroid_collision(asteroids: List[int]) -> List[int]:
  stack = []

  for asteroid in asteroids:
    if asteroid > 0 or not stack:
      stack.append(asteroid)
      continue

    should_add_asteroid = True
    while stack and stack[-1] > 0:
      asteroid_abs = abs(asteroid)
      if asteroid_abs < stack[-1]:
        should_add_asteroid = False
        break

      if asteroid_abs == stack[-1]:
        should_add_asteroid = False
        stack.pop()
        break

      stack.pop()

    if should_add_asteroid:
      stack.append(asteroid)

  return stack


if __name__ == "__main__":
  print(asteroid_collision(read_int_array(sys.argv[1])))
"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

Examples:
Input: position = [1,2,3]
Output: 1

Input: position = [2,2,2,3,3]
Output: 2

Input: position = [1,1000000000]
Output: 1

Problem source: LeetCode

Usage: min_cost_move_chips.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def min_cost_to_move_chips(position: List[int]) -> int:
  cost_odd = 0
  cost_even = 0
  target_odd = -1
  target_even = -1

  positions = {} # i: chip_count

  for idx in position:
    if idx not in positions:
      positions[idx] = 1
    else:
      positions[idx] += 1

    if idx % 2 == 1 and (target_odd == -1 or positions[idx] > positions[target_odd]):
      target_odd = idx
    elif idx % 2 == 0 and (target_even == -1 or positions[idx] > positions[target_even]):
      target_even = idx

  for i, chips in positions.items():
    if abs(target_odd - i) % 2 != 0:
      cost_odd += chips
    else:
      cost_even += chips

  return min(cost_odd, cost_even)

def min_cost_to_move_chips_2(position: List[int]) -> int:
  odd = 0
  even = 0

  for pos in position:
    if pos % 2 == 0:
      even += 1
    else:
      odd += 1

  return min(odd, even)


if __name__ == '__main__':
  print(min_cost_to_move_chips(read_int_array(sys.argv[1])))
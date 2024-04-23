"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Examples:
Input: gain = [-5,1,5,0,-7]
Output: 1

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0

Problem source: LeetCode

Usage: highest_altitude_gain.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def largestAltitude(gain: List[int]) -> int:
  max_altitude = 0
  current_altitude = 0

  for num in gain:
    current_altitude += num
    max_altitude = max(current_altitude, max_altitude)

  return max_altitude


if __name__ == "__main__":
  print(read_int_array(sys.argv[1]))
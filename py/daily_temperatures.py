"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Examples:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]

Problem source: LeetCode

Usage: daily_temperatures.py <comma_separated_values>
"""

from typing import List
from utils import read_int_array
import sys

def daily_temperatures(temperatures: List[int]) -> List[int]:
  non_solved_days = []
  answer = [0] * len(temperatures)

  for i, temperature in enumerate(temperatures):

    if len(non_solved_days) > 0 and temperature > temperatures[non_solved_days[-1]]:
      while len(non_solved_days) > 0:
        idx = non_solved_days[-1]
        if temperature > temperatures[idx]:
          answer[idx] = i - idx
          non_solved_days.pop()
        else:
          break
            
    non_solved_days.append(i)

  return answer


if __name__ == "__main__":
  print(daily_temperatures(read_int_array(sys.argv[1])))
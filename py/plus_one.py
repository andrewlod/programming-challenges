"""
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:
Input: 1,3 2,6 8,10 15,18
Output: [[1,6],[8,10],[15,18]]

Input: 1,4 4,5
Output: [[1,5]]

Problem source: LeetCode

Usage: plus_one.py <comma_separated_nums>
"""
from typing import List
from utils import read_int_array
import sys

def plus_one(digits: List[int]) -> List[int]:
  if digits[-1] < 9:
    new_digits = digits[:]
    new_digits[-1] += 1
    return new_digits

  new_digits = [0] * (len(digits))

  carry_over = True
  for i in range(len(digits)-1, -1, -1):
    if digits[i] == 9 and carry_over:
      continue

    if carry_over:
      new_digits[i] = digits[i] + 1
      carry_over = False
    else:
      new_digits[i] = digits[i]
      
  if carry_over:
    return [1] + new_digits

  return new_digits


if __name__ == "__main__":
  print(plus_one(read_int_array(sys.argv[1])))
"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Examples:
Input: num = 9669
Output: 9969

Input: num = 9996
Output: 9999

Input: num = 9999
Output: 9999

Problem source: LeetCode

Usage: maximum_69_number.py <num_of_6s_and_9s>
"""

from math import floor, log10
import sys

def maximum_69_number (num: int) -> int:
  decimal_power = 10 ** floor(log10(num))

  temp_num = num
  while decimal_power > 0 and temp_num // decimal_power == 9:
    temp_num = temp_num % decimal_power
    decimal_power //= 10

  return num + 3*decimal_power


if __name__ == '__main__':
  print(maximum_69_number(int(sys.argv[1])))
"""
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

Examples:
Input: num = 2932
Output: 52

Input: num = 4009
Output: 13

Problem source: LeetCode

Usage: min_sum_4_digit_number.py <4_digit_num>
"""

import sys

def minimum_sum(num: int) -> int:
  digits = sorted([int(n) for n in str(num)])
  num1 = 0
  num2 = 0

  for i in range(0, len(digits), 2):
    num1 = (num1 * 10) + digits[i]
    num2 = (num2 * 10) + digits[i+1]

  return num1 + num2


if __name__ == "__main__":
  print(minimum_sum(int(sys.argv[1])))
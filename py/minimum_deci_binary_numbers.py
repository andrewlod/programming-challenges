"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Examples:
Input: n = "32"
Output: 3

Input: n = "82734"
Output: 8

Input: n = "27346209830709182346"
Output: 9

Problem source: LeetCode

Usage: minimum_deci_binary_numbers.py <n>
"""

import sys

def min_partitions(n: str) -> int:
  return int(max(n))


if __name__ == '__main__':
  print(min_partitions(sys.argv[1]))
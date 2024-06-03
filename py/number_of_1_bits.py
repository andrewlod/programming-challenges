"""
Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

Examples:
Input: n = 11
Output: 3

Input: n = 128
Output: 1

Input: n = 2147483645
Output: 30

Problem source: LeetCode

Usage: number_of_1_bits.py <n>
"""

import sys

def hamming_weight(n: int) -> int:
  num_bits = 0

  while n > 0:
    num_bits += n % 2
    n //= 2

  return num_bits


if __name__ == '__main__':
  print(hamming_weight(int(sys.argv[1])))
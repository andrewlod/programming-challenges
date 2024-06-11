"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Examples:
Input: a = 2, b = 6, c = 5
Output: 3

Input: a = 4, b = 2, c = 7
Output: 1

Input: a = 1, b = 2, c = 3
Output: 0

Problem source: LeetCode

Usage: minimum_flips.py <a> <b> <c>
"""

from typing import List
from math import log2, floor
import sys

def get_bits(num: int, max_bits: int) -> List[int]:
  bits = []
  while num > 0:
    bits.append(num % 2)
    num //= 2

  return bits + [0] * (max_bits - len(bits))

def min_flips(a: int, b: int, c: int) -> int:
  max_bits = floor(log2(max(a, b, c)) + 1)
  bits_a = get_bits(a, max_bits)
  bits_b = get_bits(b, max_bits)
  bits_c = get_bits(c, max_bits)

  count = 0
  for bit_a, bit_b, bit_c in zip(bits_a, bits_b, bits_c):
    if bit_a != bit_b and bit_c == 0:
      count += 1
    elif bit_a == bit_b != bit_c:
      count += 2 - bit_c

  return count


if __name__ == "__main__":
  print(min_flips(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
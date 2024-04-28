"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Examples:
Input: m = 2
Output: [0,1,1]

Input: n = 5
Output: [0,1,1,2,1,2]

Problem source: LeetCode

Usage: counting_bits.py <n>
"""

from typing import List
import sys

def add_one(last_number: List[int], last_count: int) -> int:
  for i, num in enumerate(last_number):
    if num == 0:
      last_number[i] = 1
      last_count += 1
      return last_count

    last_number[i] = 0
    last_count -= 1

  return last_count


def count_bits(n: int) -> List[int]:
  result = [0] * (n + 1)
  last_number = [0] * 17

  for i in range(1, n + 1):
    result[i] = add_one(last_number, result[i-1])

  return result

# More efficient solution
def count_bits_2(n: int) -> List[int]:
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result


if __name__ == "__main__":
  print(count_bits(int(sys.argv[1])))
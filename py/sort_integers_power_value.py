"""
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the kth integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.

Examples:
Input: lo = 12, hi = 15, k = 2
Output: 13

Input: lo = 7, hi = 11, k = 4
Output: 7

Problem source: LeetCode

Usage: sort_integers_power_value.py <lo> <hi> <k>
"""

from functools import cmp_to_key
import sys

def get_kth(lo: int, hi: int, k: int) -> int:
  nums = [i for i in range(lo, hi+1)]
  powers = {1: 0}

  def get_power(num: int) -> int:
    nonlocal powers
    if num in powers:
      return powers[num]

    power = 0
    if num % 2 == 0:
      power = get_power(num//2) + 1
    else:
      power = get_power(num * 3 + 1) + 1

    powers[num] = power
    return power

  return sorted(nums, key=cmp_to_key(lambda a, b: get_power(a) - get_power(b)))[k-1]


if __name__ == "__main__":
  print(get_kth(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
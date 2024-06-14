"""
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Examples:
Input: nums = [1,2,3], k = 2
Output: 1

Input: nums = [2,1,8], k = 10
Output: 3

Input: nums = [1,2], k = 0
Output: 1

Problem source: LeetCode

Usage: shortest_subarray_or.py <comma_separated_nums> <k>
"""

from typing import List
from utils import read_int_array
import sys

def minimum_subarray_length(nums: List[int], k: int) -> int:
  current = 0
  length = 0
  best_length = 100
  start = 0
  bit_count = [0] * 32
  max_bit_length = 0

  def add_right(num: int):
    nonlocal current, bit_count, max_bit_length
    current |= num

    idx = 0
    while num > 0:
      bit_count[idx] += num % 2
      num //= 2
      idx += 1
    
    max_bit_length = max(max_bit_length, idx)

  def remove_left(num: int):
    nonlocal current, bit_count, max_bit_length

    idx = 0
    while num > 0:
      bit_count[idx] -= num % 2
      num //= 2
      idx += 1

    temp_curr = 0
    for i in range(max_bit_length, -1, -1):
      temp_curr <<= 1
      if bit_count[i] > 0:
        temp_curr += 1

    current = temp_curr

  for num in nums:
    add_right(num)
    length += 1

    while current >= k and length > 0 and start < len(nums):
      best_length = min(best_length, length)
      remove_left(nums[start])
      length -= 1
      start += 1

  return best_length if best_length < 100 else -1


if __name__ == "__main__":
  print(minimum_subarray_length(read_int_array(sys.argv[1]), int(sys.argv[2])))
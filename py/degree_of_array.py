"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Examples:
Input: nums = [1,2,2,3,1]
Output: 2

Input: nums = [1,2,2,3,1,4,2]
Output: 6

Problem source: LeetCode

Usage: degree_of_array.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_shortest_sub_array(nums: List[int]) -> int:
  freqs = {} # num: (freq, idx_start)
  max_freq_numbers = {} # num: (idx_start, idx_end)
  max_freq = 1

  for i, num in enumerate(nums):
    if num not in freqs:
      freqs[num] = [1, i]
    else:
      freqs[num][0] += 1

    if freqs[num][0] > max_freq:
      max_freq_numbers = {
          num: [freqs[num][1], i]
      }
      max_freq = freqs[num][0]
    elif freqs[num][0] == max_freq:
      max_freq_numbers[num] = [freqs[num][1], i]


  min_length = 2147483647

  for idx_start, idx_end in max_freq_numbers.values():
    min_length = min(min_length, idx_end - idx_start + 1)

  return min_length


if __name__ == "__main__":
  print(find_shortest_sub_array(read_int_array(sys.argv[1])))
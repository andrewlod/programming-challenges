"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

Examples:
Input: nums = [1,2,2,3,1,4]
Output: 4

Input: nums = [1,2,3,4,5]
Output: 5

Problem source: LeetCode

Usage: maximum_frequency_element_count.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def max_frequency_elements(nums: List[int]) -> int:
  freqs = {}

  for num in nums:
    if num not in freqs:
      freqs[num] = 1
    else:
      freqs[num] += 1

  max_frequency = 1
  max_count = 0

  for freq in freqs.values():
    if freq > max_frequency:
      max_frequency = freq
      max_count = max_frequency
    elif freq == max_frequency:
      max_count += max_frequency

  return max_count


if __name__ == '__main__':
  print(max_frequency_elements(read_int_array(sys.argv[1])))
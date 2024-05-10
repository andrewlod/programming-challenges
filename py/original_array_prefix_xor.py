"""
You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

Examples:
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]

Input: pref = [13]
Output: [13]

Problem source: LeetCode

Usage: original_array_prefix_xor.py <comma_separated_nums>
"""

from typing import List
from utils import read_int_array
import sys

def find_array(pref: List[int]) -> List[int]:
  result = pref[:]

  for i in range(1, len(pref)):
    result[i] = pref[i-1] ^ pref[i]

  return result


if __name__ == "__main__":
  print(find_array(read_int_array(sys.argv[1])))
"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Examples:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6, chars = ["a","2","b","2","c","3"]

Input: chars = ["a"]
Output: 1, chars = ["a"]

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4, chars = ["a","b","1","2"]

Problem source: LeetCode

Usage: string_compression.py <s>
"""

from typing import List
import sys

def compress(chars: List[str]) -> int:
  idx = 0
  current_char = chars[0]
  current_length = 0

  for char in chars:
    if char == current_char:
      current_length += 1
      continue

    chars[idx] = current_char
    idx += 1
    if current_length > 1:
      current_length_str = str(current_length)
      for length_char in current_length_str:
        chars[idx] = length_char
        idx += 1

    current_length = 1
    current_char = char

  chars[idx] = current_char
  idx += 1
  if current_length > 1:
    current_length_str = str(current_length)
    for length_char in current_length_str:
      chars[idx] = length_char
      idx += 1

  return idx


if __name__ == "__main__":
  print(compress(list(sys.argv[1])))
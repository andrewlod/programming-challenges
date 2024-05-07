"""
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.
Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

Examples:
Input: word = "abc"
Output: 5

Input: word = "bza"
Output: 7

Input: word = "zjpc"
Output: 34

Problem source: LeetCode

Usage: min_type_time_special_typewriter.py <word>
"""

import sys

def min_time_to_type(word: str) -> int:
  current_pos = 97
  seconds = 0
  higher_bound = 122
  lower_bound = 97

  for char in word:
    ascii_value = ord(char)
    clockwise = 0
    counterclockwise = 0

    if ascii_value > current_pos:
      clockwise = ascii_value - current_pos
      counterclockwise = current_pos - lower_bound + higher_bound - ascii_value + 1
    else:
      clockwise = higher_bound - current_pos + ascii_value - lower_bound + 1
      counterclockwise = current_pos - ascii_value

    seconds += min(clockwise, counterclockwise) + 1
    current_pos = ascii_value

  return seconds


if __name__ == "__main__":
  print(min_time_to_type(sys.argv[1]))
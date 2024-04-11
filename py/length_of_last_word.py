"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Examples:
Input: s = "Hello World"
Output: 5

Input: s = "   fly me   to   the moon  "
Output: 4

Problem source: LeetCode

Usage: length_of_last_word.py <word1> <word2> <word3> ...
"""

import sys

def length_of_last_word(s: str) -> int:
  return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
  print(length_of_last_word(" ".join(sys.argv[1:])))
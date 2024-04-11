"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Examples:
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "a good   example"
Output: "example good a"

Problem source: LeetCode

Usage: reverse_words.py <word1> <word2> <word3> ...
"""

import sys

def reverse_words(s: str) -> str:
  return " ".join(list(reversed(
    list(filter(lambda x: x != "", s.strip().split(" ")))
  )))


if __name__ == "__main__":
  print(reverse_words(" ".join(sys.argv[1:])))
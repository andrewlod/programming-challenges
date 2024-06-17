"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Examples:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"

Input: word = "abcd", ch = "z"
Output: "abcd"

Problem source: LeetCode

Usage: reverse_prefix_of_word.py <word> <ch>
"""

import sys

def reverse_prefix(word: str, ch: str) -> str:
  idx = 0
  try:
    idx = word.index(ch)
  except ValueError:
    return word

  return word[idx::-1] + word[idx+1:]


if __name__ == "__main__":
  print(reverse_prefix(sys.argv[1], sys.argv[2]))
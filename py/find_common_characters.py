"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Examples:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Problem source: LeetCode

Usage: find_common_characters.py <comma_separated_words>
"""

from typing import List
from utils import read_str_array
import sys

def common_chars(words: List[str]) -> List[str]:
  common = {}

  for c in words[0]:
    if c not in common:
      common[c] = 1
    else:
      common[c] += 1

  for word in words[1:]:
    new_common = {}
    for c in word:
      if c in common and common[c] > 0:
        if c not in new_common:
          new_common[c] = 1
        else:
          new_common[c] += 1

        common[c] -= 1

    common = new_common

  letters = []
  for letter, freq in common.items():
    letters += [letter] * freq

  return letters


if __name__ == "__main__":
  print(common_chars(read_str_array(sys.argv[1])))
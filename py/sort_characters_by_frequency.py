"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Examples:
Input: s = "tree"
Output: "eert"

Input: s = "cccaaa"
Output: "aaaccc"

Input: s = "Aabb"
Output: "bbAa"

Problem source: LeetCode

Usage: sort_characters_by_frequency.py <s>
"""

from functools import cmp_to_key
import sys

def frequency_sort(s: str) -> str:
  frequencies = {}

  for c in s:
    if c not in frequencies:
      frequencies[c] = 1
    else:
      frequencies[c] += 1

  sorted_frequencies = sorted(frequencies.items(), key=cmp_to_key(lambda a, b: a[1] - b[1]), reverse=True)

  word = []
  for c, frequency in sorted_frequencies:
    word.append(c * frequency)

  return "".join(word)


if __name__ == "__main__":
  print(frequency_sort(sys.argv[1]))
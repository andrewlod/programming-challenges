"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Examples:
Input: word1 = "abc", word2 = "bca"
Output: true

Input: word1 = "a", word2 = "aa"
Output: false

Input: word1 = "cabbba", word2 = "abbccc"
Output: true

Problem source: LeetCode

Usage: check_if_2_strings_are_close.py <word1> <word2>
"""

import sys

def close_strings(word1: str, word2: str) -> bool:
  if len(word1) != len(word2):
    return False

  freqs1 = [0] * 26
  freqs2 = [0] * 26

  for char in word1:
    freqs1[ord(char) - ord('a')] += 1

  for char in word2:
    freqs2[ord(char) - ord('a')] += 1

  for i in range(26):
    if (freqs1[i] > 0 and freqs2[i] == 0) or (freqs1[i] == 0 and freqs2[i] > 0):
      return False

  freqs1.sort()
  freqs2.sort()

  for i in range(26):
    if freqs1[i] != freqs2[i]:
      return False

  return True


if __name__ == "__main__":
  print(close_strings(sys.argv[1], sys.argv[2]))
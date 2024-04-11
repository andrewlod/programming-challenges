"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Examples:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Problem source: LeetCode

Usage: word_break.py <s> <dict_word_1> <dict_word_2> ...
"""

from typing import List
import sys

def solve(s: str, wordDict: List[str], found):
  if s in found:
    return found[s]

  if len(s) == 0:
    return True

  for word in wordDict:
    if s.startswith(word) and solve(s[len(word):], wordDict, found):
      found[s] = True
      return True

  found[s] = False
  return False


def word_break(s: str, wordDict: List[str]) -> bool:
  return solve(s, wordDict, {})


if __name__ == "__main__":
  print(word_break(sys.argv[1], sys.argv[2:]))
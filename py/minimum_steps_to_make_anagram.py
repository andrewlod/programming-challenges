"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Examples:
Input: s = "bab", t = "aba"
Output: 1

Input: s = "leetcode", t = "practice"
Output: 5

Input: s = "anagram", t = "mangaar"
Output: 0

Problem source: LeetCode

Usage: minimum_steps_to_make_anagram.py <s> <t>
"""
import sys

def min_steps(s: str, t: str) -> int:
  count_s = {}
  count_t = {}

  for c in s:
    if c not in count_s:
      count_s[c] = 1
    else:
      count_s[c] += 1

  for c in t:
    if c not in count_t:
      count_t[c] = 1
    else:
      count_t[c] += 1

  total = 0

  for key in count_s:
    if key not in count_t:
      total += count_s[key]
    elif count_s[key] > count_t[key]:
      total += count_s[key] - count_t[key]

  return total


if __name__ == "__main__":
  print(min_steps(
    sys.argv[1],
    sys.argv[2]
  ))
"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Examples:
Input: text1 = "abcde", text2 = "ace"
Output: 3

Input: text1 = "abc", text2 = "abc"
Output: 3

Input: text1 = "abc", text2 = "def"
Output: 0

Problem source: LeetCode

Usage: longest_common_subsequence.py <text1> <text2>
"""

from typing import List
import sys

def dp_longest_common_subsequence(text1: str, text2: str, i: int, j: int, n: int, m: int, results: List[List[int]]):
  if i >= n or j >= m:
    return 0

  if results[i][j] > -1:
    return results[i][j]

  result = 0
  if text1[i] == text2[j]:
    result = 1 + dp_longest_common_subsequence(text1, text2, i+1, j+1, n, m, results)
  else:
    result = max(
      dp_longest_common_subsequence(text1, text2, i+1, j, n, m, results),
      dp_longest_common_subsequence(text1, text2, i, j+1, n, m, results)
    )

  results[i][j] = result

  return result


def longest_common_subsequence(text1: str, text2: str) -> int:
  # Get only the common characters
  text1_characters = set()
  text2_characters = set()

  for character in text1:
    text1_characters.add(character)

  for character in text2:
    text2_characters.add(character)

  text1_new = ""
  for character in text1:
    if character in text2_characters:
      text1_new += character
  
  text1 = text1_new

  text2_new = ""
  for character in text2:
    if character in text1_characters:
      text2_new += character
  
  text2 = text2_new

  # Dynamic programming
  n = len(text1)
  m = len(text2)
  results = [
    [-1 for j in range(m)] for i in range(n)
  ] 

  return dp_longest_common_subsequence(text1, text2, 0, 0, n, m, results)


if __name__ == "__main__":
  print(longest_common_subsequence(sys.argv[1], sys.argv[2]))
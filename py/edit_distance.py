"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Examples:
Input: word1 = "horse", word2 = "ros"
Output: 3

Input: word1 = "intention", word2 = "execution"
Output: 5

Problem source: LeetCode

Usage: edit_distance.py <word1> <word2>
"""

import sys

def min_distance(word1: str, word2: str) -> int:
  m = len(word1)
  n = len(word2)
  dp = [[0 for j in range(n+1)] for i in range(m+1)]

  for i in range(1, m+1):
    dp[i][0] = i

  for j in range(1, n+1):
    dp[0][j] = j

  for i in range(1, m+1):
    for j in range(1, n+1):
      if word1[i-1] == word2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

  return dp[m][n]


if __name__ == "__main__":
  print(min_distance(sys.argv[1], sys.argv[2]))
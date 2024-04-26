"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Examples:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Problem source: LeetCode

Usage: merge_strings_alternately.py <word1> <word2>
"""

import sys

def merge_alternately(word1: str, word2: str) -> str:
  n1 = len(word1)
  n2 = len(word2)
  merged = [''] * (n1 + n2)
  ptr1 = 0
  ptr2 = 0

  while ptr1 < n1 and ptr2 < n2:
    merged[ptr1 + ptr2] = word1[ptr1]
    merged[ptr1 + ptr2 + 1] = word2[ptr2]

    ptr1 += 1
    ptr2 += 1

  while ptr1 < n1:
    merged[ptr1 + ptr2] = word1[ptr1]
    ptr1 += 1

  while ptr2 < n2:
    merged[ptr1 + ptr2] = word2[ptr2]
    ptr2 += 1

  return "".join(merged)


if __name__ == "__main__":
  print(merge_alternately(sys.argv[1], sys.argv[2]))
"""
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
Input: pattern = "IIIDIDDD"
Output: "123549876"

Input: pattern = "DDD"
Output: "4321"

Problem source: LeetCode

Usage: smallest_number_di_string.py <pattern>
"""

import sys

def smallest_number(pattern: str) -> str:
  decreasing = 0
  num = []

  for i in range(len(pattern)):
    if pattern[i] == "I":
      for j in range(decreasing+1):
        num.append(str(i-j+1))
      decreasing = 0
    else:
      decreasing += 1


  for j in range(decreasing+1):
    num.append(str(len(pattern)-j+1))

  return "".join(num)


if __name__ == "__main__":
  print(smallest_number(sys.argv[1]))
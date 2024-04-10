"""
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Problem source: LeetCode

Usage: word_search.py "a,b,c d,e,f g,h,i" <word>
"""

from typing import List
import sys

def check_recursive(start_pos: tuple[int, int], board: List[List[str]], word: str, visited: set, m: int, n: int):
  if len(word) == 0:
    return True

  x, y = start_pos

  if start_pos in visited or x >= m or x < 0 or y >= n or y < 0:
    return False
  
  character = word[0]

  if character != board[y][x]:
    return False

  visited.add(start_pos)

  rest = word[1:]

  if (check_recursive((x + 1, y), board, rest, visited, m, n) or
    check_recursive((x - 1, y), board, rest, visited, m, n) or
    check_recursive((x, y + 1), board, rest, visited, m, n) or
    check_recursive((x, y - 1), board, rest, visited, m, n)):
      return True

  visited.remove(start_pos)

  return False

def check(start_pos: tuple[int, int], board: List[List[str]], word: str, m: int, n: int):
  visited = set()
  return check_recursive(start_pos, board, word, visited, m, n)

def exist(board: List[List[str]], word: str) -> bool:
  m = len(board[0])
  n = len(board)

  for y, row in enumerate(board):
    for x, _character in enumerate(row):
      if check((x, y), board, word, m, n):
        return True

  return False

if __name__ == "__main__":
  exist([
    row.split(",") for row in sys.argv[1].split(" ")
  ], sys.argv[2])
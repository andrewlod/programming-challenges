"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Problem source: LeetCode

Usage: generate_parentheses.py <n>
"""

from typing import List
import sys

def generate_parenthesis(n: int) -> List[str]:
  words = []

  def generate(word: List[str], opened: int, closed: int):
    if closed == n:
      words.append("".join(word))
      return

    if opened == n:
      word.append(")")
      generate(word, opened, closed+1)
      word.pop()
      return

    if opened == closed:
      word.append("(")
      generate(word, opened+1, closed)
      word.pop()
      return

    word.append("(")
    generate(word, opened+1, closed)
    word.pop()

    word.append(")")
    generate(word, opened, closed+1)
    word.pop()

  w = []
  generate(w, 0, 0)
  return words


if __name__ == "__main__":
  print(generate_parenthesis(int(sys.argv[1])))
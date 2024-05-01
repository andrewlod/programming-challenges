"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Examples:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

Problem source: LeetCode

Usage: shortest_distance_to_character.py <s> <c>
"""

from typing import List
import sys

def shortest_to_char(s: str, c: str) -> List[int]:
  answer = [0] * len(s)
  char_occurrences = []

  for i, char in enumerate(s):
    if char == c:
      char_occurrences.append(i)

  for i, idx in enumerate(char_occurrences):
    before_start = 0
    if i > 0:
      before_start = (idx + char_occurrences[i-1]) // 2 + 1

    after_end = len(s)
    if i < len(char_occurrences)-1:
      after_end = (idx + char_occurrences[i+1]) // 2 + 1

    for j in range(before_start, idx):
      answer[j] = idx - j

    for j in range(idx+1, after_end):
      answer[j] = j - idx

  return answer


if __name__ == "__main__":
  print(shortest_to_char(sys.argv[1], sys.argv[2]))
"""
Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.

Examples:
Input: s = "string"
Output: "rtsng"

Input: s = "poiinter"
Output: "ponter"

Problem source: LeetCode

Usage: faulty_keyboard.py <s>
"""

import sys

def final_string(s: str) -> str:
  sections = s.split("i")
  n = len(sections)
  for i in range(1, n):
    for j in range(i):
      sections[j] = sections[j][::-1]

    sections[:i] = reversed(sections[:i])


  return "".join(sections)


if __name__ == "__main__":
  print(final_string(sys.argv[1]))
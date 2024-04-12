"""
You are given a string s, which contains stars *.

In one operation, you can:

- Choose a star in s.
- Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

- The input will be generated such that the operation is always possible.
- It can be shown that the resulting string will always be unique.

Examples:
Input: s = "leet**cod*e"
Output: "lecoe"

Input: s = "erase*****"
Output: ""

Problem source: LeetCode

Usage: remove_stars.py <str>
"""

import sys

def remove_stars(s: str) -> str:
  stack = []

  for character in s:
    if character == "*":
      stack.pop()
    else:
      stack.append(character)

  return "".join(stack)


if __name__ == "__main__":
  print(remove_stars(sys.argv[1]))
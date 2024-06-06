"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Examples:
Input: s = "Hello"
Output: "hello"

Input: s = "here"
Output: "here"

Input: s = "LOVELY"
Output: "lovely"

Problem source: LeetCode

Usage: to_lower_case.py <s>
"""
import sys

def to_lower_case(s: str) -> str:
  chars = list(s)

  for i, char in enumerate(chars):
    ascii_value = ord(char)
    if 64 < ascii_value < 91:
      chars[i] = chr(ascii_value+32)

  return "".join(chars)


if __name__ == "__main__":
  print(to_lower_case(sys.argv[1]))
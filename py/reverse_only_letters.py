"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Examples:
Input: s = "ab-cd"
Output: "dc-ba"

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Problem source: LeetCode

Usage: reverse_only_letters.py <s>
"""

import sys

def reverse_only_letters(s: str) -> str:
  n = len(s)
  left = 0
  right = n-1
  chars = list(s)

  while left < right:
    while left < right and not chars[left].isalpha():
      left += 1

    while left < right and not chars[right].isalpha():
      right -= 1

    if left < right:
      chars[left], chars[right] = chars[right], chars[left]
      left += 1
      right -= 1

  return "".join(chars)


if __name__ == "__main__":
  print(reverse_only_letters(sys.argv[1]))
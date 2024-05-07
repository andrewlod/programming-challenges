"""
You are given a string s consisting of lowercase English letters, and you are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Your task is to make s a palindrome with the minimum number of operations possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

Return the resulting palindrome string.

Examples:
Input: s = "egcfe"
Output: "efcfe"

Input: s = "abcd"
Output: "abba"

Input: s = "seven"
Output: "neven"

Problem source: LeetCode

Usage: lexicographically_smallest_palindrome.py <s>
"""

import sys

def make_smallest_palindrome(s: str) -> str:
  chars = list(s)
  n = len(chars)

  for i in range(n//2):
    l = chars[i]
    r = chars[n-1-i]

    if l == r:
      continue

    if l > r:
      chars[i] = r
    else:
      chars[n-1-i] = l

  return "".join(chars)


if __name__ == "__main__":
  print(make_smallest_palindrome(int(sys.argv[1])))
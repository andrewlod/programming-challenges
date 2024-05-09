"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Examples:
Input: n = 1
Output: 5

Input: n = 2
Output: 15

Input: n = 33
Output: 66045

Problem source: LeetCode

Usage: count_vowel_sorted_strings.py <n>
"""

import sys

letter_additions = [
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

def count_vowel_strings(n: int) -> int:
  prev_dp = [1, 1, 1, 1, 1]

  for c in range(1, n):
    additions = [0] * 5

    for i, _count in enumerate(prev_dp):
      for j, addition in enumerate(letter_additions[i]):
        additions[j] += prev_dp[i] * addition

      prev_dp[i] += additions[i]

  return sum(prev_dp)


if __name__ == '__main__':
  print(count_vowel_strings(int(sys.argv[1])))
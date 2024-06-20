"""
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

Examples:
Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
Example 2:

Input: s = "jjjj", letter = "k"
Output: 0

Problem source: LeetCode

Usage: percentage_of_letter_in_string.py <s> <letter>
"""

from collections import Counter
from math import floor
import sys

def percentage_letter(s: str, letter: str) -> int:
  counter = Counter(s)
  return floor(100 * counter[letter] / len(s))


if __name__ == "__main__":
  print(percentage_letter(sys.argv[1], sys.argv[2]))
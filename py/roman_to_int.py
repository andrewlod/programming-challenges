"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Examples:
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

Input: s = "MCMXCIV"
Output: 1994

Problem source: LeetCode

Usage: roman_to_int.py <s>
"""

import sys

roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_to_int(s: str) -> int:
  num = 0

  i = 0
  while i < len(s)-1:
    current = roman_values[s[i]]
    next_value = roman_values[s[i+1]]
    if next_value > current:
      num += next_value - current
      i += 2
    else:
      num += current
      i += 1

  if i == len(s)-1:
    num += roman_values[s[i]]

  return num


if __name__ == "__main__":
  print(roman_to_int(sys.argv[1]))
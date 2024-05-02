"""
You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without any leading zeros are different.

Examples:
Input: word = "a123bc34d8ef34"
Output: 3

Input: word = "leet1234code234"
Output: 2

Input: word = "a1b01c001"
Output: 1

Problem source: LeetCode

Usage: num_unique_numbers_in_string.py <str>
"""

import sys

def num_different_integers(word: str) -> int:
  current_num = -1
  nums = set()

  for char in word:
    if not char.isdigit():
      if current_num != -1:
        nums.add(current_num)
        current_num = -1

      continue
    
    if current_num == -1:
      current_num = 0

    current_num = (current_num * 10) + int(char)

  if current_num != -1:
    nums.add(current_num)
  
  return len(nums)


if __name__ == "__main__":
  print(num_different_integers(sys.argv[1]))
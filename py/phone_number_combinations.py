"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Examples:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]

Problem source: LeetCode

Usage: phone_number_combinations.py <string_with_digits_2_to_9>
"""

from typing import List
import sys

digit_to_letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def make_combinations(digits: str, index: int, current_word: str, combinations: List[str]):
  if index >= len(digits):
    combinations.append(current_word)
    return

  for letter in digit_to_letters[digits[index]]:
    make_combinations(digits, index + 1, current_word + letter, combinations)


def letter_combinations(digits: str) -> List[str]:
  if len(digits) < 1:
    return []

  combinations = []
  make_combinations(digits, 0, "", combinations)

  return combinations


if __name__ == "__main__":
  print(letter_combinations(sys.argv[1]))
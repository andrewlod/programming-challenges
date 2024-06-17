"""
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Examples:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"

Input: words = ["notapalindrome","racecar"]
Output: "racecar"

Input: words = ["def","ghi"]
Output: ""

Problem source: LeetCode

Usage: first_palindrome_in_array.py <word1> <word2> ...
"""

from typing import List
from utils import read_str_array
import sys

def is_palindrome(word: str) -> bool:
  n = len(word)
  for i in range(n//2):
    if word[i] != word[n-1-i]:
      return False

  return True

def firstPalindrome(words: List[str]) -> str:
  for word in words:
    if is_palindrome(word):
      return word

  return ""

if __name__ == "__main__":
  print(firstPalindrome(read_str_array(",".join(sys.argv[1:]))))
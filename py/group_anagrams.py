"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Examples:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Problem source: LeetCode

Usage: group_anagrams.py <comma_separated_strs>
"""

from typing import List
from collections import defaultdict
from utils import read_str_array
import sys

def group_anagrams(strs: List[str]) -> List[List[str]]:
  anagrams = defaultdict(list)

  for word in strs:
    anagrams["".join(sorted(word))].append(word)

  return list(anagrams.values())


if __name__ == "__main__":
  print(group_anagrams(read_str_array(sys.argv[1])))
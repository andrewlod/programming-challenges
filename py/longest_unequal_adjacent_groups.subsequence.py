"""
You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating 
subsequence
 from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

Examples:
Input: words = ["e","a","b"], groups = [0,0,1]
Output: ["e","b"]

Input: words = ["a","b","c","d"], groups = [1,0,1,1]
Output: ["a","b","c"]

Problem source: LeetCode

Usage: longest_unequal_adjacent_groups_subsequence.py <comma_separated_chars> <comma_separated_0s_and_1s>
"""

from typing import List
from utils import read_int_array, read_str_array
import sys

def get_longest_subsequence(words: List[str], groups: List[int]) -> List[str]:
  sequence = [words[0]]
  num = groups[0]

  for word, group in zip(words[1:], groups[1:]):
    if group != num:
      num = group
      sequence.append(word)

  return sequence


if __name__ == "__main__":
  print(get_longest_subsequence(read_str_array(sys.argv[1]), read_int_array(sys.argv[2])))
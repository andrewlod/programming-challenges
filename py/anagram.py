"""
This script determines if two strings `s` and `t` are anagrams.

Examples:
Input: anagram nagaram
Output: True

Input: rat car
Output: False

Problem source: LeetCode

Usage: anagram.py <s> <t>
"""

import sys

def is_anagram(s: str, t: str) -> bool:
    """
    Determines if strings `s` and `t` are anagrams.

    Parameters:
    s (str): Any string
    t (str): Any string to compare to `s`

    Returns:
    bool: Whether the two strings are anagrams
    """

    s_counts = {}

    for char in s:
        s_counts[char] = s_counts.get(char, 0) + 1

    for char in t:
        if char not in s_counts:
            return False

        s_counts[char] -= 1
        if s_counts[char] == 0:
            del s_counts[char]

    return len(s_counts) == 0

if __name__ == "__main__":
    print(is_anagram(
        sys.argv[1],
        sys.argv[2]
    ))
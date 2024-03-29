"""
Given two strings `ransomNote` and `magazine`, return true if `ransomNote` can be constructed by using the letters from `magazine` and false otherwise.

Examples:
Input: aa ab
Output: False

Input: aa aab
Output: True

Problem source: LeetCode

Usage: ransom_note.py <ransom_note> <magazine>
"""

import sys

def can_construct(ransom_note: str, magazine: str) -> bool:
    """
    Determines whether `ransom_note` can be constructed from `magazine`.

    Parameters:
    ransom_note (str): String to be constructed
    magazine (str): String to construct ransom_note from

    Returns:
    bool: Whether `ransom_note` can be constructed from the characters present in `magazine`
    """

    ransom_counts = {}
    magazine_counts = {}

    for char in ransom_note:
        if char not in ransom_counts:
            ransom_counts[char] = 0

        ransom_counts[char] += 1

    for char in magazine:
        if char not in magazine_counts:
            magazine_counts[char] = 0

        magazine_counts[char] += 1

    for [key, value] in ransom_counts.items():
        if key not in magazine_counts or magazine_counts[key] < value:
            return False

    return True

if __name__ == "__main__":
    print(can_construct(
        sys.argv[1],
        sys.argv[2]
    ))
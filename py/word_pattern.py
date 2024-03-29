"""
This script determines if two strings, `pattern` containing letters and `s` containing words separated by space, follow the same pattern.

Examples:
Input: abba "dog cat cat dog"
Output: True

Input: abba "dog cat cat fish"
Output: False

Problem source: LeetCode

Usage: word_pattern.py <pattern> <s>
"""

import sys

def word_pattern(pattern: str, s: str) -> bool:
    """
    Determines if `s` follows the same pattern as `pattern`.

    Parameters:
    pattern (str): String containing a sequence of letters
    s (str): String containing words separed by space

    Returns:
    bool: Whether the two strings follow the same pattern
    """

    s_words = s.split(" ")

    if len(s_words) != len(pattern):
        return False

    letter_map = {}
    words_found = set()

    for letter, word in zip(pattern, s_words):
        if (letter in letter_map and letter_map[letter] != word) or (letter not in letter_map and word in words_found):
            return False

        letter_map[letter] = word
        words_found.add(word)

    return True

if __name__ == "__main__":
    print(word_pattern(
        sys.argv[1],
        sys.argv[2]
    ))
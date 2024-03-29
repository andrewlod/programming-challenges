"""
This script determines if two strings `s` and `t` are isomorphic.

Examples:
Input: egg add
Output: True

Input: foo bar
Output: False

Problem source: LeetCode

Usage: isomorphic.py <s> <t>
"""

import sys

def is_isomorphic(s: str, t: str) -> bool:
    """
    Determines if strings `s` and `t` are isomorphic.

    Parameters:
    s (str): Any string
    t (str): Any string to compare to `s`

    Returns:
    bool: Whether the two strings are isomorphic
    """

    iso_map = {}
    t_mapped = set()

    for s_char, t_char in zip(s, t):
        if (s_char in iso_map and iso_map[s_char] != t_char) or (s_char not in iso_map and t_char in t_mapped):
            return False

        iso_map[s_char] = t_char
        t_mapped.add(t_char)

    return True

if __name__ == "__main__":
    print(is_isomorphic(
        sys.argv[1],
        sys.argv[2]
    ))
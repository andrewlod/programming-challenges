"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Examples:
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

Problem source: LeetCode

Usage: reverse_string_vowels.py <s>
"""

import sys

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

def reverse_vowels(s: str) -> str:
    left = 0
    right = len(s)-1

    chars = [char for char in s]

    while left < right:
        if chars[left] not in vowels:
            left += 1
            continue

        if chars[right] not in vowels:
            right -= 1
            continue

        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_vowels(sys.argv[1]))
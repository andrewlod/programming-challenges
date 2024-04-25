"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Examples:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Problem source: LeetCode

Usage: decode_string.py <s>
"""

import sys

def decode_string(s: str) -> str:
    parsing_brackets = False
    current_expression = []
    current_multiplier = 0
    new_s = []
    bracket_stack = 0

    for char in s:
        if parsing_brackets:
            if char == "]" and bracket_stack == 0:
                new_s.append(decode_string("".join(current_expression)) * current_multiplier)
                parsing_brackets = False
                current_expression = []
                current_multiplier = 0
                continue
            
            if char == "]":
                bracket_stack -= 1
            elif char == "[":
                bracket_stack += 1

            current_expression.append(char)
            continue

        if char == "[":
            parsing_brackets = True
            continue

        if char.isdigit():
            current_multiplier = current_multiplier * 10 + int(char)
        else:
            new_s.append(char)
    
    return "".join(new_s)


if __name__ == "__main__":
    print(decode_string(sys.argv[1]))
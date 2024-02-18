"""
This script checks if a given numeric sequence is additive

Examples:
Input: 347111829
Output: True

Input: 15051101152
Output: True

Input: 15141161152
Output: False

Problem source: Interview Pen (https://www.youtube.com/watch?v=GneS80iYa7I)

Usage: additive_sequence.py <numeric_sequence>
"""

from math import log10, floor
import sys

def get_number_of_characters(value: int) -> int:
    """
    Number of characters that an integer would use in a string, based on decimal numeric system.

    Parameters:
    value (int): Integer value to get number of characters

    Returns:
    int: String length of the number
    """
    return 1 + floor(log10(value))


def check_additive(s: str, first_length: int, second_length: int):
    """
    Checks if a sequence of characters is additive, given the length of the first and second numbers

    Parameters:
    s (str): Sequence of characters to be processed
    first_length (str): Length of the first number, which is a substring of s from 0 to first_length
    second_length (str): Length of the second number, which is a substring of s from first_length to (first_length + second_length)

    Returns:
    bool: Whether the two initial numbers make up an additive sequence in s
    """
    if first_length + second_length >= len(s):
        return False

    last_position = first_length + second_length

    first_number = int(s[0:first_length])
    second_number = int(s[first_length:last_position])

    while last_position < len(s):
        result = first_number + second_number
        next_amt_of_characters = get_number_of_characters(result)
        next_last_position = last_position + next_amt_of_characters

        if next_last_position > len(s):
            return False
        
        next_number = int(s[last_position:next_last_position])

        if result != next_number:
            return False
        
        first_number = second_number
        second_number = result
        last_position = next_last_position


    return True


def is_additive(s: str) -> bool:
    """
    Checks if the string s represents an additive sequence

    Parameters:
    s (str): String consisting of digit characters

    Returns:
    bool: True if s represents an additive sequence, False otherwise
    """
    if len(s) < 2:
        return False

    max_length = len(s)//2

    for first_length in range(1, max_length + 1):
        for second_length in range(1, max_length + 1):
            if check_additive(s, first_length, second_length):
                return True
            
    return False


if __name__ == "__main__":
    print(is_additive(sys.argv[1]))
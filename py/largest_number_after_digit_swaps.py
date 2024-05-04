"""
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

Examples:
Input: num = 1234
Output: 3412

Input: num = 65875
Output: 87655

Problem source: LeetCode

Usage: largest_number_after_digit_swaps.py <num>
"""

from heapq import _heapify_max, _heappop_max
import sys

def largest_integer(num: int) -> int:
    digits = [int(n) for n in str(num)]
    odds = [int(n) for n in digits if n%2 == 1]
    evens = [int(n) for n in digits if n%2 == 0]

    _heapify_max(odds)
    _heapify_max(evens)

    new_num = 0
    for digit in digits:
        n = None
        if digit % 2 == 0:
            n = _heappop_max(evens)
        else:
            n = _heappop_max(odds)

        new_num = new_num * 10 + n

    return new_num


if __name__ == '__main__':
    print(largest_integer(int(sys.argv[1])))
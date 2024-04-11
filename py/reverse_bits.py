"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Examples:
Input: n = 43261596 (00000010100101000001111010011100)
Output: 964176192 (00111001011110000010100101000000)

Input: 4294967293 (11111111111111111111111111111101)
Output: 3221225471 (10111111111111111111111111111111)

Problem source: LeetCode

Usage: reverse_bits.py <n>
"""

from typing import List
import sys

def int_to_binary(n: int) -> List[int]:
    digits = []

    while n > 0:
        digit = n % 2
        digits.append(digit)
        n //= 2

    return digits + [0] * (32 - len(digits))


def reverse_bits(n: int) -> int:
    binaryDigits = int_to_binary(n)
    num = 0

    for digit in binaryDigits:
        num <<= 1
        num += digit

    return num


if __name__ == "__main__":
    print(reverse_bits(int(sys.argv[1])))
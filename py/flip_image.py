"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].

Examples:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

Problem source: LeetCode

Usage: flip_image.py <comma_separated_row1> <comma_separated_row2> ...
"""

from typing import List
from utils import read_int_matrix
import sys

def flip_and_invert_image(image: List[List[int]]) -> List[List[int]]:
  n = len(image)

  for row in image:
    for j in range(n//2):
      row[j], row[n-j-1] = ((1 - row[n-j-1]), (1 - row[j]))
    
    if n % 2 == 1:
      row[n//2] = 1 - row[n//2]

  return image


if __name__ == '__main__':
  print(flip_and_invert_image(read_int_matrix("".join(sys.argv[1:]))))
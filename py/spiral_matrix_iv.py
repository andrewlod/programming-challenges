"""
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

Examples:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]

Problem source: LeetCode

Usage: spiral_matrix_iv.py <m> <n> <comma_separated_nums>
"""

from typing import List, Optional
from utils import ListNode, read_int_linked_list
import sys

def get_next_direction(matrix: List[List[int]], i: int, j: int, m: int, n: int, direction: int) -> int:
  if direction == 0:
    return 0 if j < n-1 and matrix[i][j+1] == -1 else 1
      
  if direction == 1:
    return 1 if i < m-1 and matrix[i+1][j] == -1 else 2
      
  if direction == 2:
    return 2 if j > 0 and matrix[i][j-1] == -1 else 3
      
  if direction == 3:
    return 3 if i > 0 and matrix[i-1][j] == -1 else 0

def spiral_matrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
  matrix = [[-1 for j in range(n)] for i in range(m)]
  i = 0
  j = 0

  direction = 0

  while head:
    matrix[i][j] = head.val
    head = head.next

    direction = get_next_direction(matrix, i, j, m, n, direction)

    if direction == 0:
      j += 1
    elif direction == 1:
      i += 1
    elif direction == 2:
      j -= 1
    elif direction == 3:
      i -= 1

  return matrix


if __name__ == "__main__":
  print(spiral_matrix(int(sys.argv[1]), int(sys.argv[2], read_int_linked_list(sys.argv[3]))))
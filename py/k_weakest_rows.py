"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Examples:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]

Problem source: LeetCode

Usage: k_weakest_rows.py "r1v1,r1v2,r1v3 r2v1,r2v2,r2v3 ..." <k>
"""

from heapq import heapify, heappop
from typing import List
from utils import read_int_matrix
import sys

def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
  soldiers_per_row = [None] * len(mat)

  for i, row in enumerate(mat):
    count = 0
    for entity in row:
      if entity == 0:
        break

      count += 1

    soldiers_per_row[i] = (count, i)

  heapify(soldiers_per_row) # Will heapify using the first element as key
  arr = []
  for i in range(k):
    arr.append(heappop(soldiers_per_row)[1])

  return arr


if __name__ == "__main__":
  print(k_weakest_rows(read_int_matrix(sys.argv[1]), int(sys.argv[2])))
"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Examples:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Problem source: LeetCode

Usage: number_of_provinces.py <comma_separated_row_1> <comma_separated_row_2> ...
"""

from typing import List
from functools import reduce
from utils import read_int_matrix
import sys

def find_province_index(provinces, index) -> int:
  if type(provinces[index]) is set:
    return index

  return find_province_index(provinces, provinces[index])


def find_circle_num(is_connected: List[List[int]]) -> int:
  provinces = [set([i]) for i in range(len(is_connected))]

  for i, row in enumerate(is_connected):
    for j in range(i + 1, len(row)):
      if row[j] == 1:
        province_idx = find_province_index(provinces, j)
        province = provinces[province_idx]

        source_province_idx = find_province_index(provinces, i)

        if province_idx == source_province_idx:
          continue

        provinces[source_province_idx].update(province)
        provinces[province_idx] = source_province_idx


  return reduce(lambda acc, val: acc + 1 if type(val) is set else acc, provinces, 0)


if __name__ == "__main__":
  print(find_circle_num(read_int_matrix(" ".join(sys.argv[1:]))))
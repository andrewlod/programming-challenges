"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Examples:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Problem source: LeetCode

Usage: interval_list_intersections.py "<start1,end1 start2,end2 ...>" <start1,end1 start2,end2 ...>
"""

from typing import List
from utils import read_int_matrix
import sys

def interval_intersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
  first_ptr = 0
  second_ptr = 0
  m = len(firstList)
  n = len(secondList)
  intersections = []

  while first_ptr < m and second_ptr < n:
    first = firstList[first_ptr]
    second = secondList[second_ptr]
    if (second[0] <= first[0] <= second[1]) or (first[0] <= second[0] <= first[1]):
      intersections.append([max(first[0], second[0]), min(first[1], second[1])])

    if first[1] < second[1]:
      first_ptr += 1
    else:
      second_ptr += 1

  return intersections


if __name__ == "__main__":
  print(interval_intersection(read_int_matrix(sys.argv[1]), read_int_matrix(sys.argv[2])))
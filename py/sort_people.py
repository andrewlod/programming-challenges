"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Examples:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]

Problem source: LeetCode

Usage: sort_people.py <comma_separated_names> <comma_separated_nums>
"""

from typing import List
from functools import cmp_to_key
from utils import read_int_array
import sys

def sort_people(names: List[str], heights: List[int]) -> List[str]:
  sorted_people = sorted(zip(names, heights), reverse=True, key=cmp_to_key(lambda a, b: a[1] - b[1]))
  return [person for person, _height in sorted_people]


if __name__ == "__main__":
  print(sort_people(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
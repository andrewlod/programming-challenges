"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Examples:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]

Problem source: LeetCode

Usage: relative_sort_array.py <comma_separated_arr1> <comma_separated_arr2>
"""

from typing import List
from utils import read_int_array
import sys

def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
  arr2_set = set(arr2)
  arr1_common = {}
  arr1_different = []

  for num in arr1:
    if num in arr2_set:
      if num not in arr1_common:
        arr1_common[num] = 1
      else:
        arr1_common[num] += 1
    else:
      arr1_different.append(num)

  arr = []

  for num in arr2:
    arr += [num] * arr1_common[num]

  return arr + list(sorted(arr1_different))


if __name__ == '__main__':
  print(relative_sort_array(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
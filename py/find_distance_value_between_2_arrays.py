"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Examples:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Problem source: LeetCode

Usage: find_distance_value_between_2_arrays.py <comma_separated_nums1> <comma_separated_nums2> <d>
"""

from typing import List
from utils import read_int_array
import sys

# Solution 1: Brute Force
def find_the_distance_value(arr1: List[int], arr2: List[int], d: int) -> int:
  count = 0
  for num1 in arr1:
    count += 1
    for num2 in arr2:
      if abs(num1 - num2) <= d:
        count -= 1
        break

  return count


# Solution 2: Sort + Binary Search
def find_the_distance_value_2(arr1: List[int], arr2: List[int], d: int) -> int:
  sorted_arr1 = sorted(arr1)
  sorted_arr2 = sorted(arr2)

  count = 0
  for num in sorted_arr1:
    left = 0
    right = len(arr2)-1
    while left < right:
      midpoint = (left + right) // 2
      val = sorted_arr2[midpoint]
      if val == num:
        left = midpoint
        break
      elif val > num:
        right = midpoint
      else:
        left = midpoint + 1

    if abs(sorted_arr2[left] - num) <= d or (left > 0 and abs(sorted_arr2[left-1] - num) <= d):
      count += 1

  return len(arr1) - count


if __name__ == "__main__":
  print(find_the_distance_value_2(read_int_array(sys.argv[1]), read_int_array(sys.argv[2]), int(sys.argv[3])))
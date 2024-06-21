"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Examples:
Input: g = [1,2,3], s = [1,1]
Output: 1

Input: g = [1,2], s = [1,2,3]
Output: 2

Problem source: LeetCode

Usage: assign_cookies.py <comma_separated_greeds> <comma_separated_cookies>
"""

from typing import List
from utils import read_int_array
import sys

def find_content_children(g: List[int], s: List[int]) -> int:
  sorted_greeds = sorted(g)
  sorted_cookies = sorted(s)
  count = 0

  while sorted_greeds and sorted_cookies:
    if sorted_greeds[-1] <= sorted_cookies[-1]:
      count += 1
      sorted_cookies.pop()

    sorted_greeds.pop()

  return count


if __name__ == "__main__":
  print(find_content_children(read_int_array(sys.argv[1]), read_int_array(sys.argv[2])))
"""
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.

Examples:
Input: cookies = [8,15,10,20,8], k = 2
Output: 31

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7

Problem source: LeetCode

Usage: fair_distribution_of_cookies.py <comma_separated_cookies> <k>
"""

from typing import List
from utils import read_int_array
import sys

def distribute_cookies(cookies: List[int], k: int) -> int:
  children = [0] * k
  n = len(cookies)
  average = sum(cookies) // k
  
  def dfs(i: int, zero_count: int) -> int:
    nonlocal children, n, average
    if i == n:
      return max(children)

    unfairness = float('inf')
    if n - i < zero_count:
      return unfairness

    next_children = [j for j in range(k) if children[j] < average]
    for j in next_children:
      is_kid_j_zero = int(children[j] == 0)

      children[j] += cookies[i]
      unfairness = min(unfairness, dfs(i+1, zero_count - is_kid_j_zero))
      children[j] -= cookies[i]

    return unfairness

  return dfs(0, k)


if __name__ == "__main__":
  print(distribute_cookies(read_int_array(sys.argv[1]), int(sys.argv[2])))
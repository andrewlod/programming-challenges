"""
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

Examples:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]

Input: arr = [1,7], k = 1
Output: [1,7]

Problem source: LeetCode

Usage: k_th_smallest_prime_fraction.py <comma_separated_primes> <k>
"""

from heapq import heappush, heappop
from typing import List
from utils import read_int_array
import sys

def kth_smallest_prime_fraction(arr: List[int], k: int) -> List[int]:
  if k == 1:
      return [arr[0], arr[-1]]

  numbers = []

  for i, _ in enumerate(arr):
    for j in range(len(arr)-1, i-1, -1):
      heappush(numbers, (arr[i]/arr[j], i, j))

  for i in range(k-1):
    heappop(numbers)

  _, i, j = heappop(numbers)
  return [arr[i], arr[j]]


if __name__ == '__main__':
  print(kth_smallest_prime_fraction(read_int_array(sys.argv[1]), int(sys.argv[2])))
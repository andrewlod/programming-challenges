"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Examples:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

Problem source: LeetCode

Usage: grumpy_bookstore_owner.py <comma_separated_customers> <comma_separated_grumpy> <minutes>
"""

from typing import List
from utils import read_int_array
import sys

def max_satisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
  best_grumpy = 0
  start = 0
  end = 0
  best_start = 0
  best_end = 0
  current_grumpy = 0

  for customer in customers:
    if end - start == minutes:
      if current_grumpy > best_grumpy:
        best_grumpy = current_grumpy
        best_start = start
        best_end = end

      if grumpy[start] == 1:
        current_grumpy -= customers[start]

      start += 1

    if grumpy[end] == 1:
      current_grumpy += customers[end]

    end += 1
      
  if current_grumpy > best_grumpy:
    best_grumpy = current_grumpy
    best_start = start
    best_end = end

  total = 0
  for i, customer in enumerate(customers):
    if best_start <= i < best_end or not grumpy[i]:
      total += customer

  return total


if __name__ == "__main__":
  print(max_satisfied(read_int_array(sys.argv[1]), read_int_array(sys.argv[2]), int(sys.argv[3])))
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Examples:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Input: candidates = [2], target = 1
Output: []

Problem source: LeetCode

Usage: combination_sum.py <comma_separated_nums> <target>
"""

from typing import List
from utils import read_int_array
import sys

def backtrack(candidates: List[int], idx: int, current_sum: int, current_selected: List[int], target: int, combinations: List[List[int]]):
  current_sum += candidates[idx]
  current_selected.append(candidates[idx])
  if current_sum == target:
    combinations.append(current_selected[:])
    current_selected.pop()
    return

  for i in range(idx, len(candidates)):
    if current_sum + candidates[i] <= target:
      backtrack(candidates, i, current_sum, current_selected, target, combinations)
  
  current_selected.pop()

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
  current_selected = []
  combinations = []
  for i in range(len(candidates)):
    backtrack(candidates, i, 0, current_selected, target, combinations)

  return combinations


if __name__ == "__main__":
  print(combination_sum(read_int_array(sys.argv[1]), int(sys.argv[2])))
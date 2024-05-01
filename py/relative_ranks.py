"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Examples:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

Problem source: LeetCode

Usage: relative_ranks.py <comma_separated_nums>
"""

from typing import List
from functools import cmp_to_key
from utils import read_int_array
import sys

def find_relative_ranks(score: List[int]) -> List[str]:
  scores_idxs = enumerate(score)
  sorted_scores = sorted(scores_idxs, key=cmp_to_key(lambda a, b: a[1] - b[1]), reverse=True)

  placement_labels = ["Gold Medal", "Silver Medal", "Bronze Medal"]
  placements = [0] * len(score)

  for i, pair in enumerate(sorted_scores):
    idx, _ = pair
    if i < 3:
      placements[idx] = placement_labels[i]
    else:
      placements[idx] = str(i + 1)

  return placements


if __name__ == "__main__":
  print(find_relative_ranks(read_int_array(sys.argv[1])))
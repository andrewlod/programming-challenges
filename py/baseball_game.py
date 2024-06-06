"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

Examples:
Input: ops = ["5","2","C","D","+"]
Output: 30

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27

Input: ops = ["1","C"]
Output: 0

Problem source: LeetCode

Usage: baseball_game.py <comma_separated_strs>
"""

from typing import List
from utils import read_str_array
import sys

def cal_points(operations: List[str]) -> int:
  score = 0
  previous_scores = []

  for operation in operations:
    if operation == "+":
      new_score = previous_scores[-1] + previous_scores[-2]
      previous_scores.append(new_score)
      score += new_score
    elif operation == "D":
      new_score = previous_scores[-1] * 2
      previous_scores.append(new_score)
      score += new_score
    elif operation == "C":
      removed_score = previous_scores.pop()
      score -= removed_score
    else:
      new_score = int(operation)
      previous_scores.append(new_score)
      score += new_score

  return score


if __name__ == "__main__":
  print(cal_points(read_str_array(sys.argv[1])))